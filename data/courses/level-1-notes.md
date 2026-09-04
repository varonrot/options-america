# Level 1 — Buying Call Option

Source course ID: `50160`

Legacy course route:
`/courses/options-trading-course-level-1-buying-call-option/`

## Extraction status

The legacy course HTML exposes the ordered curriculum and legacy lesson IDs. The WordPress WXR export exposes MasterStudy `stm-lessons` metadata, including `type`, `duration`, `video_type`, and `lesson_vimeo_url`.

Verified examples:

| Order | Lesson ID | Title | Type | Duration | Vimeo |
|---:|---:|---|---|---|---|
| 1 | 50337 | What will we learn in this course? | video | 2 min | present in WXR |
| 8 | 50344 | 5 reasons why to trade options | video | 3 min | `930554634` |
| 9 | 50345 | Risk Disclaimer | video | 3 min | `931720532` |
| 10 | 50346 | Welcome to the first part of the long call strategy | video | 2 min | present in WXR |

## Player architecture

The new course player should use one shell rather than one hand-written HTML page per video:

- ordered curriculum in a data file
- Vimeo iframe/player loaded from each lesson's metadata
- active lesson highlighted in the curriculum
- Previous / Next controls
- listen for Vimeo `ended`
- mark the current lesson complete locally
- automatically load the next video lesson after completion
- quizzes and text lessons render in the same content area instead of the Vimeo iframe
- keep the legacy lesson IDs available for URL/SEO migration

Do not infer Vimeo IDs from lesson IDs. They must be extracted from `lesson_vimeo_url` in the WXR export.