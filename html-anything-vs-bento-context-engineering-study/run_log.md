# 运行日志

所有时间均为 2026-07-25 UTC。叙述使用中文，CLI 原始输出保留标准技术术语。

## 上游固定版本
- `html-anything`: `1896831a62670eed7424b8f8e37e56c66cbf2351`
- `bento`: `17121c260966752a2eda58dc2a919ae908872ef4`

## html-anything 安装、构建与测试
命令：`npm ci && npm run build && npm test`
```text
npm warn Unknown env config "http-proxy". This will stop working in the next major version of npm.
npm warn EBADENGINE Unsupported engine {
npm warn EBADENGINE   package: 'pdfjs-dist@5.7.284',
npm warn EBADENGINE   required: { node: '>=22.13.0 || >=24' },
npm warn EBADENGINE   current: { node: 'v20.20.2', npm: '11.4.2' }
npm warn EBADENGINE }

added 73 packages, and audited 74 packages in 5s

15 packages are looking for funding
  run `npm fund` for details

1 low severity vulnerability

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
npm notice
npm notice New minor version of npm available! 11.4.2 -> 11.18.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.18.0
npm notice To update run: npm install -g npm@11.18.0
npm notice
npm warn Unknown env config "http-proxy". This will stop working in the next major version of npm.

> html-anything@0.1.0 build
> tsc

npm warn Unknown env config "http-proxy". This will stop working in the next major version of npm.

> html-anything@0.1.0 test
> node --test

TAP version 13
# Warning: UnknownErrorException: Ensure that the `standardFontDataUrl` API parameter is provided.
# Warning: UnknownErrorException: Ensure that the `standardFontDataUrl` API parameter is provided.
# Warning: UnknownErrorException: Ensure that the `standardFontDataUrl` API parameter is provided.
# Warning: UnknownErrorException: Ensure that the `standardFontDataUrl` API parameter is provided.
# Subtest: pdf parser extracts text + headings from the synthetic fixture
ok 1 - pdf parser extracts text + headings from the synthetic fixture
  ---
  duration_ms: 541.227349
  ...
# Subtest: docx parser extracts headings + plain text from the synthetic fixture
ok 2 - docx parser extracts headings + plain text from the synthetic fixture
  ---
  duration_ms: 454.861078
  ...
# Subtest: htmlize fallback: source-prompt resolution covers pdf-document + docx-document
ok 3 - htmlize fallback: source-prompt resolution covers pdf-document + docx-document
  ---
  duration_ms: 0.471941
  ...
# Subtest: htmlize auto style selector routes major source families
ok 4 - htmlize auto style selector routes major source families
  ---
  duration_ms: 3.970405
  ...
# Subtest: style catalog stays in sync with style types, prompts, examples, and previews
ok 5 - style catalog stays in sync with style types, prompts, examples, and previews
  ---
  duration_ms: 53.342748
  ...
# Subtest: htmlize injects the selected style prompt into the LLM request
ok 6 - htmlize injects the selected style prompt into the LLM request
  ---
  duration_ms: 10.870043
  ...
# Subtest: htmlize injects the explicit digital-eguide style prompt into the LLM request
ok 7 - htmlize injects the explicit digital-eguide style prompt into the LLM request
  ---
  duration_ms: 9.888074
  ...
# Subtest: htmlize injects packaged reference HTML for reference-backed styles
ok 8 - htmlize injects packaged reference HTML for reference-backed styles
  ---
  duration_ms: 12.876341
  ...
# Subtest: style reference assets are style-scoped and map to output assets paths
ok 9 - style reference assets are style-scoped and map to output assets paths
  ---
  duration_ms: 4.025399
  ...
# Subtest: checked-in example pages are complete and have parseable inline scripts
ok 10 - checked-in example pages are complete and have parseable inline scripts
  ---
  duration_ms: 313.840151
  ...
# Subtest: jsonl parser ingests the synthetic JSONL event stream + infers schema + outliers
ok 11 - jsonl parser ingests the synthetic JSONL event stream + infers schema + outliers
  ---
  duration_ms: 14.27199
  ...
# Subtest: log parser detects + parses an Apache/Nginx-style access log
ok 12 - log parser detects + parses an Apache/Nginx-style access log
  ---
  duration_ms: 20.846972
  ...
# Subtest: log parser routes a structured error log to the event-stream pack
ok 13 - log parser routes a structured error log to the event-stream pack
  ---
  duration_ms: 7.450988
  ...
# Subtest: registry exposes jsonl + log parser names
ok 14 - registry exposes jsonl + log parser names
  ---
  duration_ms: 0.623777
  ...
# Subtest: experiential parser includes derived leaderboards in full data
ok 15 - experiential parser includes derived leaderboards in full data
  ---
  duration_ms: 32.30298
  ...
# Subtest: finance parser routes a bank-transaction CSV to the bank-transactions content type
ok 16 - finance parser routes a bank-transaction CSV to the bank-transactions content type
  ---
  duration_ms: 49.684442
  ...
# Subtest: finance parser routes an invoices CSV to the invoices content type with aging buckets
ok 17 - finance parser routes an invoices CSV to the invoices content type with aging buckets
  ---
  duration_ms: 13.325645
  ...
# Subtest: finance parser routes a QuickBooks GL export with a hierarchical account tree
ok 18 - finance parser routes a QuickBooks GL export with a hierarchical account tree
  ---
  duration_ms: 6.495609
  ...
# Subtest: finance parser refuses non-finance CSVs (issue trackers, plain tabular)
ok 19 - finance parser refuses non-finance CSVs (issue trackers, plain tabular)
  ---
  duration_ms: 2.159795
  ...
# Subtest: htmlize family routing: finance content types resolve to _finance.md
ok 20 - htmlize family routing: finance content types resolve to _finance.md
  ---
  duration_ms: 2.366889
  ...
# Subtest: registry exposes finance parser before generic csv
ok 21 - registry exposes finance parser before generic csv
  ---
  duration_ms: 0.433529
  ...
# Subtest: wechat parser routes a WeChatMsg-style CSV to the relationship report shape
ok 22 - wechat parser routes a WeChatMsg-style CSV to the relationship report shape
  ---
  duration_ms: 3214.159011
  ...
# Subtest: whatsapp parser emits the shared relationship-report aggregations
ok 23 - whatsapp parser emits the shared relationship-report aggregations
  ---
  duration_ms: 44.757783
  ...
# Subtest: registry exposes wechat parser before whatsapp, csv, docx, and research
ok 24 - registry exposes wechat parser before whatsapp, csv, docx, and research
  ---
  duration_ms: 0.649048
  ...
# Subtest: planning parser routes a founder .ics calendar to ics-calendar with weeks + back-to-back blocks
ok 25 - planning parser routes a founder .ics calendar to ics-calendar with weeks + back-to-back blocks
  ---
  duration_ms: 26.724996
  ...
# Subtest: planning parser detects a Linear-style issue CSV and aggregates owner load + stale items
ok 26 - planning parser detects a Linear-style issue CSV and aggregates owner load + stale items
  ---
  duration_ms: 22.911571
  ...
# Subtest: planning parser does NOT claim a generic data CSV (header without status+title shape)
ok 27 - planning parser does NOT claim a generic data CSV (header without status+title shape)
  ---
  duration_ms: 2.062639
  ...
# Subtest: registry exposes planning parser before csv (so issue trackers route correctly)
ok 28 - registry exposes planning parser before csv (so issue trackers route correctly)
  ---
  duration_ms: 0.431417
  ...
# Subtest: knowledge-base parser walks the synthetic notes-vault and builds a backlink graph
ok 29 - knowledge-base parser walks the synthetic notes-vault and builds a backlink graph
  ---
  duration_ms: 30.563359
  ...
# Subtest: knowledge-base parser refuses an empty directory and a non-directory
ok 30 - knowledge-base parser refuses an empty directory and a non-directory
  ---
  duration_ms: 1.499774
  ...
# Subtest: knowledge-base family prompts are present on disk
ok 31 - knowledge-base family prompts are present on disk
  ---
  duration_ms: 1.722886
  ...
# Subtest: geo parser ingests a synthetic GPX run with stats + splits + elevation profile
ok 32 - geo parser ingests a synthetic GPX run with stats + splits + elevation profile
  ---
  duration_ms: 13.243773
  ...
# Subtest: geo parser ingests a multi-day itinerary CSV with day buckets + conflict detection
ok 33 - geo parser ingests a multi-day itinerary CSV with day buckets + conflict detection
  ---
  duration_ms: 6.345384
  ...
# Subtest: geo parser detects KML + GPX by extension+content
ok 34 - geo parser detects KML + GPX by extension+content
  ---
  duration_ms: 3.179332
  ...
# Subtest: geo parser refuses generic data CSVs (no date+location signal)
ok 35 - geo parser refuses generic data CSVs (no date+location signal)
  ---
  duration_ms: 1.092605
  ...
# Subtest: registry exposes geo parser before planning + finance + csv
ok 36 - registry exposes geo parser before planning + finance + csv
  ---
  duration_ms: 0.391621
  ...
# Subtest: geo family prompts are present on disk
ok 37 - geo family prompts are present on disk
  ---
  duration_ms: 2.40923
  ...
# Subtest: sensitive parser routes the synthetic medical-visit fixture to medical-visit
ok 38 - sensitive parser routes the synthetic medical-visit fixture to medical-visit
  ---
  duration_ms: 6.567922
  ...
# Subtest: sensitive parser routes the synthetic lab-results fixture to lab-results
ok 39 - sensitive parser routes the synthetic lab-results fixture to lab-results
  ---
  duration_ms: 7.33793
  ...
# Subtest: sensitive parser routes the synthetic legal-chronology fixture to legal-chronology
ok 40 - sensitive parser routes the synthetic legal-chronology fixture to legal-chronology
  ---
  duration_ms: 7.878955
  ...
# Subtest: registry order: sensitive comes before finance and markdown
ok 41 - registry order: sensitive comes before finance and markdown
  ---
  duration_ms: 0.312818
  ...
# Subtest: sensitive family prompts are present on disk
ok 42 - sensitive family prompts are present on disk
  ---
  duration_ms: 1.066212
  ...
# Subtest: experiential parser routes the synthetic Amazon order fixture to amazon-orders
ok 43 - experiential parser routes the synthetic Amazon order fixture to amazon-orders
  ---
  duration_ms: 17.134041
  ...
# Subtest: experiential (amazon-orders) detection beats finance + csv on Amazon-shaped CSVs
ok 44 - experiential (amazon-orders) detection beats finance + csv on Amazon-shaped CSVs
  ---
  duration_ms: 0.336326
  ...
# Subtest: amazon-orders prompt is present on disk
ok 45 - amazon-orders prompt is present on disk
  ---
  duration_ms: 0.880263
  ...
# Subtest: ai-chat-export parser routes a synthetic ChatGPT conversations.json to chatgpt-export
ok 46 - ai-chat-export parser routes a synthetic ChatGPT conversations.json to chatgpt-export
  ---
  duration_ms: 16.881748
  ...
# Subtest: ai-chat-export parser routes a markdown User:/Assistant: chat log to ai-chat-export
ok 47 - ai-chat-export parser routes a markdown User:/Assistant: chat log to ai-chat-export
  ---
  duration_ms: 5.950372
  ...
# Subtest: ai-chat-export parser does NOT claim a generic JSON / non-chat .md
ok 48 - ai-chat-export parser does NOT claim a generic JSON / non-chat .md
  ---
  duration_ms: 6.263756
  ...
# Subtest: registry order: ai-chat-export comes before slack/sensitive/markdown/json
ok 49 - registry order: ai-chat-export comes before slack/sensitive/markdown/json
  ---
  duration_ms: 0.387116
  ...
# Subtest: ai-chat-export family prompts are present on disk
ok 50 - ai-chat-export family prompts are present on disk
  ---
  duration_ms: 1.168359
  ...
# Subtest: kindle parser routes My Clippings.txt to kindle-highlights and pre-aggregates the family contract
ok 51 - kindle parser routes My Clippings.txt to kindle-highlights and pre-aggregates the family contract
  ---
  duration_ms: 17.684731
  ...
# Subtest: kindle parser refuses a generic .txt that does not look like My Clippings
ok 52 - kindle parser refuses a generic .txt that does not look like My Clippings
  ---
  duration_ms: 1.006636
  ...
# Subtest: registry order: kindle comes before whatsapp + text + research
ok 53 - registry order: kindle comes before whatsapp + text + research
  ---
  duration_ms: 0.907772
  ...
# Subtest: kindle-highlights prompt is present on disk
ok 54 - kindle-highlights prompt is present on disk
  ---
  duration_ms: 0.820165
  ...
# Subtest: experiential parser routes the synthetic YouTube watch-history fixture to youtube-watch-history
ok 55 - experiential parser routes the synthetic YouTube watch-history fixture to youtube-watch-history
  ---
  duration_ms: 45.897754
  ...
# Subtest: experiential parser does NOT confuse YouTube + Spotify JSON
ok 56 - experiential parser does NOT confuse YouTube + Spotify JSON
  ---
  duration_ms: 39.18258
  ...
# Subtest: youtube-watch-history prompt is present on disk
ok 57 - youtube-watch-history prompt is present on disk
  ---
  duration_ms: 0.793959
  ...
# Subtest: youtube-watch-history output.html renders the required family sections
ok 58 - youtube-watch-history output.html renders the required family sections
  ---
  duration_ms: 5.977698
  ...
# Subtest: experiential parser routes the synthetic browser-history fixture to browser-history
ok 59 - experiential parser routes the synthetic browser-history fixture to browser-history
  ---
  duration_ms: 39.017974
  ...
# Subtest: browser-history detection does not steal Spotify or YouTube JSON
ok 60 - browser-history detection does not steal Spotify or YouTube JSON
  ---
  duration_ms: 47.669314
  ...
# Subtest: browser-history prompt is present on disk
ok 61 - browser-history prompt is present on disk
  ---
  duration_ms: 0.924999
  ...
# Subtest: kindle-highlights output.html renders the required family sections
ok 62 - kindle-highlights output.html renders the required family sections
  ---
  duration_ms: 4.816493
  ...
# Subtest: ai-chat-export output.html files render the required family sections
ok 63 - ai-chat-export output.html files render the required family sections
  ---
  duration_ms: 9.933302
  ...
# Subtest: social-payments parser routes a synthetic Venmo CSV
ok 64 - social-payments parser routes a synthetic Venmo CSV
  ---
  duration_ms: 28.085781
  ...
# Subtest: photos-takeout parser routes the synthetic Google Photos Takeout fixture to google-photos-takeout
ok 65 - photos-takeout parser routes the synthetic Google Photos Takeout fixture to google-photos-takeout
  ---
  duration_ms: 186.268137
  ...
# Subtest: photos-takeout parser refuses an empty directory and a non-directory
ok 66 - photos-takeout parser refuses an empty directory and a non-directory
  ---
  duration_ms: 2.08408
  ...
# Subtest: google-photos-takeout prompt is present on disk
ok 67 - google-photos-takeout prompt is present on disk
  ---
  duration_ms: 1.280125
  ...
# Subtest: vcard parser routes a multi-card .vcf to vcard-contacts and pre-aggregates the family contract
ok 68 - vcard parser routes a multi-card .vcf to vcard-contacts and pre-aggregates the family contract
  ---
  duration_ms: 18.506353
  ...
# Subtest: vcard parser refuses a non-vCard text file
ok 69 - vcard parser refuses a non-vCard text file
  ---
  duration_ms: 2.229896
  ...
# Subtest: registry exposes vcard parser before generic text
ok 70 - registry exposes vcard parser before generic text
  ---
  duration_ms: 0.501077
  ...
# Subtest: vcard-contacts prompt is present on disk
ok 71 - vcard-contacts prompt is present on disk
  ---
  duration_ms: 0.788181
  ...
# Subtest: vcard parser handles folded continuation lines + repeated typed fields
ok 72 - vcard parser handles folded continuation lines + repeated typed fields
  ---
  duration_ms: 4.270756
  ...
# Subtest: linkedin-connections detection routes Connections.csv through experiential
ok 73 - linkedin-connections detection routes Connections.csv through experiential
  ---
  duration_ms: 25.117683
  ...
# Subtest: linkedin-connections detection ignores generic CSVs without LinkedIn headers
ok 74 - linkedin-connections detection ignores generic CSVs without LinkedIn headers
  ---
  duration_ms: 4.705199
  ...
# Subtest: linkedin-connections prompt is present on disk
ok 75 - linkedin-connections prompt is present on disk
  ---
  duration_ms: 0.61553
  ...
# Subtest: vcard-contacts output.html renders the required family sections + offline rules
ok 76 - vcard-contacts output.html renders the required family sections + offline rules
  ---
  duration_ms: 4.136541
  ...
# Subtest: rideshare-history parser routes the synthetic Uber CSV
ok 77 - rideshare-history parser routes the synthetic Uber CSV
  ---
  duration_ms: 56.753922
  ...
# Subtest: rideshare-history parser routes a synthetic Lyft CSV
ok 78 - rideshare-history parser routes a synthetic Lyft CSV
  ---
  duration_ms: 15.627199
  ...
# Subtest: rideshare-history parser refuses non-rideshare CSVs (bank, plain tabular)
ok 79 - rideshare-history parser refuses non-rideshare CSVs (bank, plain tabular)
  ---
  duration_ms: 7.441248
  ...
# Subtest: registry exposes rideshare-history parser before finance + csv
ok 80 - registry exposes rideshare-history parser before finance + csv
  ---
  duration_ms: 0.337821
  ...
# Subtest: rideshare-history prompt is present on disk
ok 81 - rideshare-history prompt is present on disk
  ---
  duration_ms: 1.908172
  ...
1..81
# tests 81
# suites 0
# pass 81
# fail 0
# cancelled 0
# skipped 0
# todo 0
# duration_ms 6105.243034
```

## Bento 安装、单文件构建
命令：`npm ci && npm run build:single`
```text
npm warn Unknown env config "http-proxy". This will stop working in the next major version of npm.

added 128 packages, and audited 129 packages in 3s

8 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
npm warn Unknown env config "http-proxy". This will stop working in the next major version of npm.

> bento-slides@1.0.9 build:single
> tsc -b && SINGLEFILE=1 vite build --outDir dist-single && mv dist-single/index.html dist-single/Bento_Slides.bento.html && node ../scripts/postbuild-compress.mjs dist-single/Bento_Slides.bento.html

vite v7.3.6 building client environment for production...
transforming...
node_modules/@daybrush/utils/dist/utils.esm.js (158:30): A comment

"/*#__PURE__*/"

in "node_modules/@daybrush/utils/dist/utils.esm.js" contains an annotation that Rollup cannot interpret due to the position of the comment. The comment will be removed to avoid issues.
✓ 68 modules transformed.
rendering chunks...
[plugin vite:singlefile] 

[plugin vite:singlefile] Inlining: index-fU-dVkqE.js
[plugin vite:singlefile] Inlining: style-k3wiy3mg.css
computing gzip size...
dist-single/index.html  1,270.26 kB │ gzip: 446.57 kB
✓ built in 4.99s
compressed shell: 1185KB → 587KB (js 1089KB→551KB, css 90KB→26KB)
```

## 确定性三场景生成
命令：`python3 scripts/generate_benchmark.py ...`
```text
已生成：/workspace/research/html-anything-vs-bento-context-engineering-study/artifacts/html_anything/dashboard.html（2459 字节）
已生成：/workspace/research/html-anything-vs-bento-context-engineering-study/artifacts/bento/dashboard.bento.html（603746 字节）
已生成：/workspace/research/html-anything-vs-bento-context-engineering-study/artifacts/html_anything/brief.html（2581 字节）
已生成：/workspace/research/html-anything-vs-bento-context-engineering-study/artifacts/bento/brief.bento.html（603788 字节）
已生成：/workspace/research/html-anything-vs-bento-context-engineering-study/artifacts/html_anything/slides.html（2461 字节）
已生成：/workspace/research/html-anything-vs-bento-context-engineering-study/artifacts/bento/slides.bento.html（603724 字节）
```

## 产物验证
命令：`python3 scripts/validate_artifacts.py .`
```json
[
  {
    "文件": "artifacts/bento/brief.bento.html",
    "字节": 603788,
    "标签数": 24,
    "最大DOM深度": 5,
    "相对依赖": [],
    "硬约束通过": true,
    "Bento页数": 3
  },
  {
    "文件": "artifacts/bento/dashboard.bento.html",
    "字节": 603746,
    "标签数": 24,
    "最大DOM深度": 5,
    "相对依赖": [],
    "硬约束通过": true,
    "Bento页数": 3
  },
  {
    "文件": "artifacts/bento/slides.bento.html",
    "字节": 603724,
    "标签数": 24,
    "最大DOM深度": 5,
    "相对依赖": [],
    "硬约束通过": true,
    "Bento页数": 3
  },
  {
    "文件": "artifacts/html_anything/brief.html",
    "字节": 2581,
    "标签数": 32,
    "最大DOM深度": 8,
    "相对依赖": [],
    "硬约束通过": true,
    "Bento页数": null
  },
  {
    "文件": "artifacts/html_anything/dashboard.html",
    "字节": 2459,
    "标签数": 32,
    "最大DOM深度": 8,
    "相对依赖": [],
    "硬约束通过": true,
    "Bento页数": null
  },
  {
    "文件": "artifacts/html_anything/slides.html",
    "字节": 2461,
    "标签数": 32,
    "最大DOM深度": 8,
    "相对依赖": [],
    "硬约束通过": true,
    "Bento页数": null
  }
]
```

## Mock R2 验证
命令：`scripts/publish_r2_mock.sh artifacts /tmp/html-study-r2-staging`
```text
Mock R2 暂存完成：7 个 HTML 对象；目录：/tmp/html-study-r2-staging
SHA-256 校验：7 个对象全部通过。
```
