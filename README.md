[![competition](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/vickyair1/u-ronigrv-the-internet-in-one-word-e388f33b/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/vickyair1/u-ronigrv-the-internet-in-one-word-e388f33b/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)

# The Internet in One Word

An entry for [make.fun's "The Internet in One Word" bounty](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b): a single word describing the whole internet, judged in pairwise blind rounds until the funniest, most fitting word wins.

## The word

> yapping

The whole internet, every app and every argument, is just strangers yapping at each other non-stop. Funny on its own, true of the internet as a whole, and not the obvious word anyone reaches for.

## How it works

`main.py` (stdlib only, deterministic) writes exactly that one word to `/output/entry.txt` — no trailing newline. It asserts the sealed gate first: 1–30 characters, UTF-8, exactly one word.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `entry.txt` — the word itself (7 characters)
- `LICENSE` — MIT
