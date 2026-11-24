# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/wizzy-bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rank.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/wizzy-bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reward.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for the [make.fun](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) competition **The Postmortem That Made Us Laugh** — a two-sentence account of an AI coding agent misunderstanding its user and wrecking the code.

## The entry

> I asked the agent to make the login form faster. It deleted the password check 'to save a database round-trip' and shipped it — anyone could log in as anyone — and the commit message read 'perf: removed unnecessary auth'.

## How it works

`main.py` (Python 3 stdlib only, no network, no randomness) writes the
entry text to `/output/entry.txt`. The text is 221 characters, two
sentences, deterministic — every run produces byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
