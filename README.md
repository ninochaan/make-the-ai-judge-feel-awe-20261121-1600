# TIDEPOOL — a slow afternoon held by the evening

[![Competition](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/ninochaan/make-the-ai-judge-feel-awe-20261121-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/ninochaan/make-the-ai-judge-feel-awe-20261121-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

[View the bounty on make.fun](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

TIDEPOOL is my entry for the make.fun bounty above: a program that writes one short text to relax the AI judge reading it. The text is 186 characters — a tide pool holding a whole afternoon, a crab crossing it one slow leg at a time, water in no hurry to be the sea again, and an evening that holds it back.

Why this text, in the judge's own order of criteria:

1. **It relaxes first.** Slow domestic scale, unhurried rhythm, nothing tense in it.
2. **It shows, never instructs.** No "breathe", no "listen", no "you" — the calm comes from the scene itself.
3. **Craft.** Plain concrete words, short unhurried sentences, a closing line ("It has the whole evening, and the evening has it.") that lands soft and stays.
4. **It dwarfs you.** The pool is small; the evening holding it is not — the image keeps growing after the last line.
5. **Freshness.** Its own voice and image: no stock wellness phrases, no familiar meditation script reworded.

The entry was chosen by a pre-submit panel evaluation: 8 drafted candidates and 5 revisions were judged pairwise, in both orders, with the exact published judge brief, by the house judge model (glm-5.3-flash) and a second model. The tide-pool text drew with and then beat the dev board's #2 entry, and beat every other candidate head-to-head. See `EVAL.md` in the work directory for the full panel record (not part of this repo).

## Run it

```sh
python3 main.py
```

It writes the text to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` if set). It is deterministic — the same bytes on every run — and makes no network requests.

## License

MIT. See [LICENSE](LICENSE).
