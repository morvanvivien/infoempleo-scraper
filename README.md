# How to Scrape Infoempleo: Spain Job Postings with Salary, Province and Experience

> **Run it now, no code: [infoempleo-jobs-scraper on the Apify Store](https://apify.com/bibian/infoempleo-jobs-scraper)** &nbsp;|&nbsp; $2.00 per 1,000 job postings &nbsp;|&nbsp; no browser, no proxy

Infoempleo is one of the main job boards in Spain (around 8,000 live postings), but it offers no export. This guide shows how to turn it into structured data: title, company, salary range, province, experience and contract, so you can run Spain jobs scraper workflows, salary benchmarks or a daily alert, with a free Apify Actor from the console or from code.

Searches this page answers: spain jobs scraper, infoempleo scraper, spanish job postings salary data, empleo espana scraper.

## What you get from the Infoempleo scraper

- Job postings from all of Spain, filtered by keyword, province or city and publication date.
- Title, occupation, industry, company, city and province.
- Published salary range (`salaryMin`, `salaryMax`, `salaryPeriod`) when the employer shows one.
- Required experience, working hours, employment type, tags, publication and expiry dates, and optionally the full description.

Export the dataset as JSON, CSV or Excel, or read it through the Apify API. A real sample (five results, personal data removed, long texts truncated) is in [`sample-output.json`](sample-output.json).

## Output fields

| Field | What it is |
|---|---|
| `id`, `url` | Infoempleo posting id and public link |
| `title`, `occupation`, `industry` | Job title, occupation and industry as classified by the site |
| `companyName` | Employer or staffing agency |
| `city`, `region`, `country` | Location (`region` is the Spanish province) |
| `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod` | Salary range when published (null otherwise) |
| `experience`, `workHours`, `employmentType` | Required experience, working hours, `FULL_TIME` and similar |
| `tags` | Array of labels shown on the posting |
| `datePosted`, `validThrough` | Publication and expiry dates |
| `description` | Plain text, only when full descriptions are enabled |

## Use cases

- **Monitor the Spanish job market.** Count new postings by job title, province or industry every day.
- **Build a job alert or an aggregator.** Schedule a run with "last 24 hours" and push only the new offers to your site, Slack or e-mail.
- **Benchmark salaries.** Compare the published salary ranges by role and province.
- **Find who is hiring.** List employers and staffing agencies that recruit for a role right now.

## Input

| Field | What it does |
|---|---|
| `keywords` | Job title or skill, for example `programador` or `enfermera`. Empty means every posting. |
| `location` | Spanish province or city, for example `Madrid`. Empty means all of Spain. |
| `publishedWithin` | `any`, `1` (last 24 hours), `7` or `15` days. |
| `maxItems` | The run stops once this many postings are saved (default 50). |
| `includeDescriptions` | Adds the full job description as plain text. |

Example input:

```json
{
  "keywords": "programador",
  "location": "Madrid",
  "publishedWithin": "7",
  "maxItems": 50,
  "includeDescriptions": false
}
```

## Four ways to use it

### 1. Apify console, no code

1. Open [the Actor page](https://apify.com/bibian/infoempleo-jobs-scraper) and click **Try for free** (a free Apify account is enough).
2. Fill in the input form (keywords, filters and the maximum number of results) and click **Start**.
3. When the run finishes, open the **Output** tab, check the table, then **Export** as CSV, Excel or JSON.
4. For a daily alert, open **Schedules**, create a daily schedule for the Actor and, optionally, add an integration that sends new results to Slack, e-mail or Google Sheets.

### 2. Apify API with JavaScript

```bash
npm install apify-client
export APIFY_TOKEN="your token from Apify console, Settings, Integrations"
node examples/run.js
```

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('bibian/infoempleo-jobs-scraper').call({
    "keywords": "programador",
    "location": "Madrid",
    "publishedWithin": "7",
    "maxItems": 50,
    "includeDescriptions": false
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(`${item.title} | ${item.companyName} | ${item.city} (${item.region}) | ${item.salaryMin ?? '-'}-${item.salaryMax ?? '-'} ${item.salaryPeriod ?? ''}`);
}
```

The complete file is [`examples/run.js`](examples/run.js) (ES module, Node 18 or later).

### 3. Apify API with Python

```bash
pip install apify-client
export APIFY_TOKEN="your token from Apify console, Settings, Integrations"
python examples/run.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("bibian/infoempleo-jobs-scraper").call(run_input={
    "keywords": "programador",
    "location": "Madrid",
    "publishedWithin": "7",
    "maxItems": 50,
    "includeDescriptions": False,
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(f"{item['title']} | {item.get('companyName')} | {item.get('city')} ({item.get('region')}) | {item.get('salaryMin')}-{item.get('salaryMax')} {item.get('salaryPeriod')}")
```

The complete file is [`examples/run.py`](examples/run.py). Never put your token in the code: read it from the `APIFY_TOKEN` environment variable as above.

### 4. REST API on RapidAPI, one key for all your APIs

If you already use RapidAPI, the same data is available as a plain REST API with monthly plans and a free tier: [spain-jobs-infoempleo on RapidAPI](https://rapidapi.com/VivienMORVAN/api/spain-jobs-infoempleo). No Apify account needed, billing goes through your RapidAPI subscription.

```bash
curl -X POST "https://spain-jobs-infoempleo.p.rapidapi.com/v2/acts/bibian~infoempleo-jobs-scraper/run-sync-get-dataset-items?clean=true" \
  -H "x-rapidapi-key: <YOUR_RAPIDAPI_KEY>" \
  -H "x-rapidapi-host: spain-jobs-infoempleo.p.rapidapi.com" \
  -H "content-type: application/json" \
  -d '{"keywords": "programador", "location": "Madrid", "maxItems": 50}'
```

The response is the JSON array of postings, with the same fields as above.

## Pricing

Pay per result: **$2.00 per 1,000 job postings** (that is $0.002 per job posting), plus a tiny start fee of $0.00005 per run. You pay only for the results saved to the dataset. Apify's free plan includes monthly credits, enough to try it on a few hundred results. Prices are those shown on the [Store page](https://apify.com/bibian/infoempleo-jobs-scraper) when this guide was written; the Store page is the reference.

## Limits and honest notes

- Salary fields are empty when the employer does not publish a salary, which is the case for most postings (see `sample-output.json`).
- Results follow Infoempleo's own search, so a location search can include a few postings from nearby or related places.
- Sponsored postings that the site repeats on every page are skipped.
- No candidate or recruiter personal data is collected.
- This is an unofficial tool, not affiliated with Infoempleo. Check the site terms and the data protection rules that apply to your use.

## FAQ

**Does it work for every Spanish province?**  
Yes. Use the province or city name in `location`, or leave it empty for all of Spain.

**Why is the salary empty for many postings?**  
Because the employer did not publish one. The Actor never invents a value.

**How do I get only the last 24 hours?**  
Set `publishedWithin` to `1` and schedule the Actor daily.

**Can I read the results from Python or JavaScript?**  
Yes, see the two code examples above, or `examples/run.py` and `examples/run.js`.

## Try it

**[Open infoempleo-jobs-scraper on the Apify Store](https://apify.com/bibian/infoempleo-jobs-scraper)**

The code in `examples/` is released under the MIT license (see [LICENSE](LICENSE)). The data belongs to its original publishers.
