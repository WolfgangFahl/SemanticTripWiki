# SemanticTripWiki

SemanticTripWiki shows [Reel Driven Development](https://wiki.bitplan.com/index.php/Reel_Driven_Development) (RDD) by example: a [Semantic MediaWiki](https://www.semantic-mediawiki.org) for the documentation of trips is specified by recorded walks - reels - and set up from that specification with a one line install.

| | |
| :--- | :--- |
| **PyPi** | [![PyPI Status](https://img.shields.io/pypi/v/SemanticTripWiki.svg)](https://pypi.python.org/pypi/SemanticTripWiki/) [![License](https://img.shields.io/github/license/WolfgangFahl/SemanticTripWiki.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![pypi](https://img.shields.io/pypi/pyversions/SemanticTripWiki)](https://pypi.org/project/SemanticTripWiki/) [![format](https://img.shields.io/pypi/format/SemanticTripWiki)](https://pypi.org/project/SemanticTripWiki/) [![downloads](https://img.shields.io/pypi/dd/SemanticTripWiki)](https://pypi.org/project/SemanticTripWiki/) |
| **GitHub** | [![Github Actions Build](https://github.com/WolfgangFahl/SemanticTripWiki/actions/workflows/build.yml/badge.svg)](https://github.com/WolfgangFahl/SemanticTripWiki/actions/workflows/build.yml) [![Release](https://img.shields.io/github/v/release/WolfgangFahl/SemanticTripWiki)](https://github.com/WolfgangFahl/SemanticTripWiki/releases) [![Contributors](https://img.shields.io/github/contributors/WolfgangFahl/SemanticTripWiki)](https://github.com/WolfgangFahl/SemanticTripWiki/graphs/contributors) [![Last Commit](https://img.shields.io/github/last-commit/WolfgangFahl/SemanticTripWiki)](https://github.com/WolfgangFahl/SemanticTripWiki/commits/) [![GitHub issues](https://img.shields.io/github/issues/WolfgangFahl/SemanticTripWiki.svg)](https://github.com/WolfgangFahl/SemanticTripWiki/issues) [![GitHub closed issues](https://img.shields.io/github/issues-closed/WolfgangFahl/SemanticTripWiki.svg)](https://github.com/WolfgangFahl/SemanticTripWiki/issues/?q=is%3Aissue+is%3Aclosed) |
| **Code** | [![style-black](https://img.shields.io/badge/%20style-black-000000.svg)](https://github.com/psf/black) [![imports-isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/) |
| **Docs** | [![API Docs](https://img.shields.io/badge/API-Documentation-blue)](https://WolfgangFahl.github.io/SemanticTripWiki/) [![formatter-docformatter](https://img.shields.io/badge/%20formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter) [![style-google](https://img.shields.io/badge/%20style-google-3666d6.svg)](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings) |

## Reel Driven Development
A reel is a recorded walk through existing systems with narration. The reel is the specification: its manifest `reel.yaml` lists every visited page with time, url and summary, so that a human or an AI agent can work from it. See [Reel Driven Development](https://wiki.bitplan.com/index.php/Reel_Driven_Development) and the tools in [reel-driven-development](https://github.com/WolfgangFahl/reel-driven-development).

The reels of this project:
* [2026-09-11 TripContext](https://rdd.bitplan.com/reels/2026-09-11-TripContext/) - the walk through the earlier trip wikis that specifies the trip wiki: trips, legs and locations with maps

Every issue of this project points to the reel that specifies or shows it.

## From reel to wiki
1. the reel specifies the model
2. the model is the [TripContext](https://contexts.bitplan.com/index.php/TripContext) of the [MetaModel](https://contexts.bitplan.com/index.php/MetaModel), kept as SiDIF in [sidif](sidif)
3. [ypgen](https://wiki.bitplan.com/index.php/Ypgen) generates the wiki pages from the model into [wikibackup](wikibackup)
4. [scripts/setup](scripts/setup) sets up a [Canasta](https://canasta.wiki) wiki and restores these pages

## Setup
```bash
curl -fsSL https://raw.githubusercontent.com/WolfgangFahl/SemanticTripWiki/main/scripts/setup | bash
```
The prerequisites - macOS or Linux, bash, curl, docker with docker compose - are checked first; see [SemanticTripWiki](https://wiki.bitplan.com/index.php/SemanticTripWiki) on wiki.bitplan.com.

## Demo
[stw.bitplan.com](https://stw.bitplan.com)

## Documentation
[Wiki](https://wiki.bitplan.com/index.php/SemanticTripWiki)

### Authors
* [Wolfgang Fahl](http://www.bitplan.com/Wolfgang_Fahl)
