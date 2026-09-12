(() => {
  const SUPABASE_URL = 'https://analkikdsytxkavvmulf.supabase.co';
  const SUPABASE_PUBLISHABLE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFuYWxraWtkc3l0eGthdnZtdWxmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ4MjUyNjAsImV4cCI6MjA4MDQwMTI2MH0.o-Ohv-CbL-RAf7DY1h1kFAHawTLpNiCU066RaDhl6zI';
  const GOOGLE_CLIENT_ID = '860183970535-8ljc09tb2uhc0q4c9vrober3dosgmmh8.apps.googleusercontent.com';
  const APP_KEY = 'options-america';
  const SDK_VERSION = '2.116.0';
  let client = null;
  let sdkPromise = null;
  let googlePromise = null;
  let rawNonce = null;

  function escapeHtml(value) {
    return String(value ?? '').replace(/[&<>"']/g, char => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    })[char]);
  }

  function safeImageUrl(value) {
    try {
      const url = new URL(String(value || ''));
      return url.protocol === 'https:' ? escapeHtml(url.href) : '';
    } catch (_) {
      return '';
    }
  }

  function loadScript(id, src) {
    const existing = document.getElementById(id);
    if (existing) {
      if (existing.dataset.loaded === 'true') return Promise.resolve();
      return new Promise((resolve, reject) => {
        existing.addEventListener('load', resolve, { once: true });
        existing.addEventListener('error', reject, { once: true });
      });
    }
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.id = id;
      script.src = src;
      script.async = true;
      script.addEventListener('load', () => {
        script.dataset.loaded = 'true';
        resolve();
      }, { once: true });
      script.addEventListener('error', reject, { once: true });
      document.head.appendChild(script);
    });
  }

  async function getClient() {
    if (client) return client;
    if (!sdkPromise) {
      sdkPromise = loadScript(
        'options-america-supabase',
        `https://cdn.jsdelivr.net/npm/@supabase/supabase-js@${SDK_VERSION}/dist/umd/supabase.js`
      );
    }
    await sdkPromise;
    if (!window.supabase?.createClient) throw new Error('Account service is unavailable.');
    client = window.supabase.createClient(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY, {
      auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true }
    });
    client.auth.onAuthStateChange(() => setTimeout(refreshAuthUI, 0));
    return client;
  }

  async function loadGoogle() {
    if (window.google?.accounts?.id) return;
    if (!googlePromise) {
      googlePromise = loadScript('options-america-google-identity', 'https://accounts.google.com/gsi/client');
    }
    await googlePromise;
  }

  function randomNonce() {
    const bytes = crypto.getRandomValues(new Uint8Array(32));
    let binary = '';
    bytes.forEach(byte => { binary += String.fromCharCode(byte); });
    return btoa(binary).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/g, '');
  }

  async function sha256Hex(value) {
    const encoded = new TextEncoder().encode(value);
    const hash = await crypto.subtle.digest('SHA-256', encoded);
    return Array.from(new Uint8Array(hash)).map(byte => byte.toString(16).padStart(2, '0')).join('');
  }

  async function registerAccess(authClient) {
    const { error } = await authClient.rpc('register_app_access', {
      p_app_key: APP_KEY,
      p_signup_source: 'google',
      p_landing_path: `${location.pathname}${location.search}`
    });
    if (error) console.warn('Options America access tracking failed', error);
  }

  function ensureDialog() {
    let dialog = document.getElementById('oaAuthDialog');
    if (dialog) return dialog;
    dialog = document.createElement('dialog');
    dialog.id = 'oaAuthDialog';
    dialog.className = 'oa-auth-dialog';
    dialog.innerHTML = `
      <div class="oa-auth-card">
        <button class="oa-auth-close" type="button" aria-label="Close">×</button>
        <span class="oa-auth-mark">↗</span>
        <h2>Sign in to Options America</h2>
        <p>Use your Google account to keep one account across Options America and our trading tools.</p>
        <div class="oa-google-host" data-google-host></div>
        <p class="oa-auth-error" role="alert" hidden></p>
        <small>Signing in does not restrict access to the free courses.</small>
      </div>`;
    document.body.appendChild(dialog);
    dialog.querySelector('.oa-auth-close')?.addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => {
      if (event.target === dialog) dialog.close();
    });
    return dialog;
  }

  function showError(message) {
    const box = ensureDialog().querySelector('.oa-auth-error');
    if (!box) return;
    box.textContent = message || 'Google sign-in could not be completed.';
    box.hidden = false;
  }

  async function finishGoogleCredential(response) {
    try {
      if (!response?.credential || !rawNonce) throw new Error('Google did not return a valid sign-in response.');
      const authClient = await getClient();
      const { data, error } = await authClient.auth.signInWithIdToken({
        provider: 'google',
        token: response.credential,
        nonce: rawNonce
      });
      rawNonce = null;
      if (error) throw error;
      if (!data?.session) throw new Error('No account session was created.');
      await registerAccess(authClient);
      ensureDialog().close();
      await refreshAuthUI();
    } catch (error) {
      rawNonce = null;
      console.error('Options America Google sign-in failed', error);
      showError(error?.message);
    }
  }

  async function beginGoogleLogin() {
    const dialog = ensureDialog();
    const errorBox = dialog.querySelector('.oa-auth-error');
    if (errorBox) errorBox.hidden = true;
    if (!dialog.open) dialog.showModal();
    try {
      await Promise.all([getClient(), loadGoogle()]);
      rawNonce = randomNonce();
      const hashedNonce = await sha256Hex(rawNonce);
      window.google.accounts.id.initialize({
        client_id: GOOGLE_CLIENT_ID,
        callback: finishGoogleCredential,
        auto_select: false,
        cancel_on_tap_outside: false,
        context: 'signin',
        ux_mode: 'popup',
        nonce: hashedNonce,
        use_fedcm_for_prompt: true
      });
      const host = dialog.querySelector('[data-google-host]');
      host.innerHTML = '';
      window.google.accounts.id.renderButton(host, {
        type: 'standard', theme: 'outline', size: 'large', text: 'signin_with',
        shape: 'pill', logo_alignment: 'left', width: 260
      });
    } catch (error) {
      console.error('Options America account UI failed', error);
      showError('Account service is temporarily unavailable. Please try again.');
    }
  }

  function userLabel(user) {
    return user?.user_metadata?.full_name || user?.user_metadata?.name || user?.email || 'Account';
  }

  function renderSignedOut(slot) {
    slot.innerHTML = '<button class="oa-login-button" type="button">Sign in</button>';
    slot.querySelector('button')?.addEventListener('click', beginGoogleLogin);
  }

  function renderSignedIn(slot, user) {
    const label = userLabel(user);
    const firstName = label.split(/\s+/)[0] || 'Account';
    const picture = safeImageUrl(user.user_metadata?.avatar_url || user.user_metadata?.picture || '');
    slot.innerHTML = `
      <button class="oa-user-button" type="button" aria-expanded="false">
        ${picture ? `<img src="${picture}" alt="">` : '<span class="oa-user-avatar">✓</span>'}
        <span>${escapeHtml(firstName)}</span><span aria-hidden="true">▾</span>
      </button>
      <div class="oa-user-menu">
        <strong>${escapeHtml(label)}</strong>
        <span>${escapeHtml(user.email || '')}</span>
        <a class="oa-dashboard-link" href="/dashboard/" style="display:flex;align-items:center;justify-content:space-between;margin-top:14px;padding:11px 12px;border-radius:9px;background:#fff5d7;color:#0d4f87;font-weight:800;text-decoration:none">Student Dashboard <span aria-hidden="true">→</span></a>
        <button type="button" data-oa-signout>Sign out</button>
      </div>`;
    const trigger = slot.querySelector('.oa-user-button');
    const menu = slot.querySelector('.oa-user-menu');
    trigger?.addEventListener('click', event => {
      event.stopPropagation();
      const open = menu.classList.toggle('open');
      trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    slot.querySelector('[data-oa-signout]')?.addEventListener('click', async () => {
      const authClient = await getClient();
      await authClient.auth.signOut();
      try { window.google?.accounts?.id?.disableAutoSelect?.(); } catch (_) {}
      renderSignedOut(slot);
    });
    document.addEventListener('click', event => {
      if (!slot.contains(event.target)) {
        menu.classList.remove('open');
        trigger?.setAttribute('aria-expanded', 'false');
      }
    });
  }

  async function refreshAuthUI() {
    const slots = document.querySelectorAll('[data-options-auth]');
    if (!slots.length) return;
    try {
      const authClient = await getClient();
      const { data: { session }, error } = await authClient.auth.getSession();
      if (error) throw error;
      for (const slot of slots) {
        if (session?.user) renderSignedIn(slot, session.user);
        else renderSignedOut(slot);
      }
      window.dispatchEvent(new CustomEvent('oa:authchange', { detail: { user: session?.user || null } }));
      if (session?.user) await registerAccess(authClient);
    } catch (error) {
      console.warn('Options America account state unavailable', error);
      slots.forEach(renderSignedOut);
    }
  }

  async function getCurrentUser() {
    try {
      const authClient = await getClient();
      const { data: { session } } = await authClient.auth.getSession();
      return session?.user || null;
    } catch (_) {
      return null;
    }
  }


  async function loadVideoProgress(courseSlug, lessonNumber) {
    try {
      const authClient = await getClient();
      const { data: { session } } = await authClient.auth.getSession();
      if (!session?.user) return [];
      let query = authClient.from('options_course_video_progress')
        .select('course_slug,lesson_number,vimeo_id,position_seconds,duration_seconds,watched_percent,completed,updated_at')
        .order('updated_at', { ascending: false });
      if (courseSlug) query = query.eq('course_slug', String(courseSlug));
      if (lessonNumber) query = query.eq('lesson_number', Number(lessonNumber));
      const { data, error } = await query;
      if (error) throw error;
      return data || [];
    } catch (error) {
      console.warn('Options America progress load failed', error);
      return [];
    }
  }

  async function saveVideoProgress(progress) {
    try {
      const authClient = await getClient();
      const { data: { session } } = await authClient.auth.getSession();
      if (!session?.user) return false;
      const input = Array.isArray(progress) ? progress : [progress];
      const rows = input.filter(Boolean).map(item => ({
        user_id: session.user.id,
        course_slug: String(item.course_slug || item.slug || ''),
        lesson_number: Math.max(1, Number(item.lesson_number || item.lesson) || 1),
        vimeo_id: item.vimeo_id ? String(item.vimeo_id) : null,
        position_seconds: Math.max(0, Number(item.position_seconds ?? item.position) || 0),
        duration_seconds: Math.max(0, Number(item.duration_seconds ?? item.duration) || 0),
        watched_percent: Math.min(100, Math.max(0, Number(item.watched_percent ?? item.percent) || 0)),
        completed: Boolean(item.completed),
        updated_at: item.updated_at || new Date().toISOString()
      })).filter(row => row.course_slug);
      if (!rows.length) return false;
      const { error } = await authClient.from('options_course_video_progress')
        .upsert(rows, { onConflict: 'user_id,course_slug,lesson_number' });
      if (error) throw error;
      return true;
    } catch (error) {
      console.warn('Options America progress save failed', error);
      return false;
    }
  }

  function addAuthSlots() {
    document.querySelectorAll('.site-header .nav').forEach(nav => {
      if (nav.querySelector('[data-options-auth]')) return;
      const slot = document.createElement('div');
      slot.className = 'oa-auth-slot';
      slot.dataset.optionsAuth = '';
      const cta = nav.querySelector(':scope > .btn');
      if (cta) nav.insertBefore(slot, cta);
      else nav.appendChild(slot);
    });
    refreshAuthUI();
  }

  window.optionsAmericaAuth = { beginGoogleLogin, refreshAuthUI, getCurrentUser, loadVideoProgress, saveVideoProgress };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', addAuthSlots, { once: true });
  else addAuthSlots();
})();
