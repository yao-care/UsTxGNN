# TxGNN 國際化 SOP - 從初始化包建立地區藥品老藥新用預測系統

## 目標

將此初始化包轉換為您國家的藥品老藥新用預測系統。

**使用方式**：
1. 解壓縮 TxGNN_init.zip
2. 閱讀本文件，按照階段化流程執行
3. 將 `.template` 檔案改名並填入當地資訊
4. 執行預測流程

---

## 一、元件分類總覽

### 1.1 通用元件（直接使用，約 60-70%）

| 類別 | 檔案 | 說明 |
|------|------|------|
| **TxGNN 知識圖譜** | `data/node.csv`, `data/kg.csv` | 知識圖譜基礎資料（需下載） |
| **詞彙表提取** | `scripts/prepare_external_data.py` | 從 TxGNN 提取 DrugBank/疾病詞彙 |
| **藥名正規化** | `src/txgnn/mapping/normalizer.py` | 通用藥名標準化 |
| **DrugBank 映射** | `src/txgnn/mapping/drugbank_mapper.py` | 成分 → DrugBank ID |
| **KG 預測** | `src/txgnn/predict/repurposing.py` | 知識圖譜方法 |
| **DL 預測** | `src/txgnn/predict/txgnn_model.py` | 深度學習方法 |
| **通用收集器** | `collectors/clinicaltrials.py`, `pubmed.py`, `drugbank.py`, `ictrp.py` | 全球資料來源 |
| **收集器基類** | `src/txgnn/collectors/base.py` | 收集器介面 |

### 1.2 需在地化元件（約 30-40%）

| 類別 | 模板檔案 | 需修改內容 |
|------|----------|------------|
| **專案設定** | `pyproject.toml.template` | 專案名稱 |
| **欄位映射** | `config/fields.yaml.template` | 藥監局資料欄位對應 |
| **資料載入** | `src/txgnn/data/loader.py.template` | 載入邏輯 |
| **疾病映射** | `src/txgnn/mapping/disease_mapper.py.template` | DISEASE_DICT（當地語言→英文） |
| **資料處理** | `scripts/process_fda_data.py.template` | ZIP/JSON 解析 |
| **預測腳本** | `scripts/run_kg_prediction.py.template` | 微調欄位名稱 |
| **FHIR 生成** | `scripts/generate_fhir_resources.py.template` | URL 和管轄區域 |
| **新聞同義詞** | `data/news/synonyms.json.template` | 疾病/藥物同義詞 |
| **網站設定** | `docs/_config.yml.template` | 標題、URL |
| **SMART App** | `docs/smart/launch.html.template` | Client ID |
| **CI/CD** | `.github/workflows/pages.yml.template` | 部署設定 |

---

## 二、階段化實施流程

### Phase 0：專案初始化

**目標**：設定專案基礎

#### 步驟：

1. **重新命名專案**
   ```bash
   # 建議命名：{Country}TxGNN
   # 例：JpTxGNN, KrTxGNN, ThTxGNN
   mv TxGNN_init {Country}TxGNN
   cd {Country}TxGNN
   ```

2. **設定 pyproject.toml**
   ```bash
   mv pyproject.toml.template pyproject.toml
   # 編輯 pyproject.toml，修改 name 和 description
   ```

3. **下載 TxGNN 資料**
   ```bash
   mkdir -p data
   curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
   curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"
   ```

4. **安裝依賴**
   ```bash
   uv sync
   ```

**品質檢查點**：
- [ ] 專案已重新命名
- [ ] `pyproject.toml` 已修改
- [ ] `uv sync` 執行成功
- [ ] TxGNN 資料下載完成（node.csv ~15MB, kg.csv ~500MB）

---

### Phase 1：FDA 資料整合

**目標**：整合當地藥監局資料

#### 1.1 調查資料來源

常見藥監局資料來源：

| 國家 | 藥監局 | 資料來源 |
|------|--------|----------|
| 日本 | PMDA | https://www.pmda.go.jp/ |
| 韓國 | MFDS | https://nedrug.mfds.go.kr/ |
| 泰國 | Thai FDA | https://www.fda.moph.go.th/ |

**產出**：記錄資料來源 URL、格式、欄位說明

#### 1.2 建立欄位映射設定

```bash
mv config/fields.yaml.template config/fields.yaml
# 編輯 fields.yaml，填入欄位對應
```

**fields.yaml 範例（日本 PMDA）**：
```yaml
country_code: JP
language: ja
regulatory_agency: PMDA

field_mapping:
  license_id: "承認番号"
  brand_name_local: "販売名"
  brand_name_en: "一般名"
  ingredients: "有効成分"
  indication: "効能・効果"
  dosage_form: "剤形"
  status: "承認状況"

withdrawn_statuses:
  - "取消"
  - "回収"
```

#### 1.3 實作資料載入器

```bash
mv src/txgnn/data/loader.py.template src/txgnn/data/loader.py
# 編輯 loader.py，實作載入邏輯
```

#### 1.4 實作資料處理腳本

```bash
mv scripts/process_fda_data.py.template scripts/process_fda_data.py
# 編輯並執行
uv run python scripts/process_fda_data.py
```

**品質檢查點**：
- [ ] `config/fields.yaml` 建立完成
- [ ] `loader.py` 能正確載入資料
- [ ] `process_fda_data.py` 執行成功
- [ ] `data/raw/{country}_fda_drugs.json` 產生

---

### Phase 2：疾病映射

**目標**：建立當地語言 → 英文疾病對照

#### 2.1 建立 DISEASE_DICT

```bash
mv src/txgnn/mapping/disease_mapper.py.template src/txgnn/mapping/disease_mapper.py
# 編輯 disease_mapper.py，填入 DISEASE_DICT
```

**目標數量**：150-200 個疾病詞條

**分類建議**：

| 分類 | 建議數量 |
|------|----------|
| 心血管系統 | 15-20 |
| 呼吸系統 | 10-15 |
| 消化系統 | 15-20 |
| 神經系統 | 10-15 |
| 精神疾病 | 8-12 |
| 內分泌系統 | 10-15 |
| 肌肉骨骼 | 10-15 |
| 皮膚疾病 | 10-15 |
| 泌尿系統 | 8-12 |
| 眼科 | 5-8 |
| 耳鼻喉 | 5-8 |
| 感染症 | 10-15 |
| 過敏 | 5-8 |
| 婦科 | 8-12 |
| 腫瘤/癌症 | 10-15 |
| 一般症狀 | 15-20 |

#### 2.2 建立新聞同義詞

```bash
mv data/news/synonyms.json.template data/news/synonyms.json
# 編輯 synonyms.json，填入當地語言同義詞
```

**品質檢查點**：
- [ ] DISEASE_DICT 有 150+ 詞條
- [ ] 涵蓋所有主要疾病分類
- [ ] `synonyms.json` 建立完成

---

### Phase 3：KG 預測流程

**目標**：執行知識圖譜預測

#### 執行步驟：

```bash
# 1. 準備詞彙表
uv run python scripts/prepare_external_data.py

# 2. 設定預測腳本
mv scripts/run_kg_prediction.py.template scripts/run_kg_prediction.py
# 編輯並執行

# 3. 執行預測
uv run python scripts/run_kg_prediction.py
```

#### 預期產出：

| 檔案 | 預期內容 |
|------|----------|
| `data/external/drugbank_vocab.csv` | ~7,958 個藥物 |
| `data/external/disease_vocab.csv` | ~17,081 個疾病 |
| `data/external/drug_disease_relations.csv` | ~80,127 個關係 |
| `data/processed/repurposing_candidates.csv` | 視藥品數量而定 |

**品質檢查點**：
- [ ] 詞彙表正確產生
- [ ] `repurposing_candidates.csv` 產生
- [ ] DrugBank 映射率 > 30%
- [ ] 疾病映射率 > 20%

---

### Phase 4：網站與 FHIR

**目標**：部署文件網站與 FHIR API

#### 4.1 Jekyll 設定

```bash
mv docs/_config.yml.template docs/_config.yml
# 編輯 _config.yml，修改標題、URL、語言
```

#### 4.2 FHIR 資源設定

```bash
mv scripts/generate_fhir_resources.py.template scripts/generate_fhir_resources.py
# 編輯 BASE_URL 和 JURISDICTION
uv run python scripts/generate_fhir_resources.py
```

#### 4.3 SMART App 設定

```bash
mv docs/smart/launch.html.template docs/smart/launch.html
# 編輯 CLIENT_ID
```

#### 4.4 本地測試

```bash
cd docs
bundle install
bundle exec jekyll serve
# 訪問 http://localhost:4000
```

**品質檢查點**：
- [ ] Jekyll 本地建置成功
- [ ] `/fhir/metadata` 可存取
- [ ] FHIR 資源正確產生

---

### Phase 5：證據收集

**目標**：設定證據收集器

#### 5.1 建立當地 FDA 收集器

建立 `src/txgnn/collectors/{country}fda.py`：

```python
from .base import BaseCollector, CollectorResult

class {Country}FDACollector(BaseCollector):
    source_name = "{country}fda"

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        # 實作搜尋邏輯
        pass
```

#### 5.2 區域臨床試驗註冊

ICTRP 涵蓋的區域註冊：
- 日本：JPRN (UMIN-CTR, JapicCTI)
- 韓國：CRIS
- 泰國：TCTR

**品質檢查點**：
- [ ] 當地 FDA 收集器建立
- [ ] ClinicalTrials.gov 收集器正常
- [ ] PubMed 收集器正常

---

### Phase 6：新聞監測

**目標**：設定健康新聞監測

#### 6.1 設定關鍵字模式

建立 `scripts/generate_news_keywords.py`，參考 TwTxGNN 版本。

#### 6.2 新增當地新聞來源

建立 `scripts/fetchers/{country}_news.py`

**品質檢查點**：
- [ ] `keywords.json` 產生
- [ ] 新聞爬蟲正常運作

---

### Phase 7：驗證與部署

**目標**：端對端驗證並部署

#### 7.1 設定 GitHub Actions

```bash
mv .github/workflows/pages.yml.template .github/workflows/pages.yml
# 編輯部署設定
```

#### 7.2 完整流程測試

```bash
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py
uv run python scripts/generate_fhir_resources.py
```

#### 7.3 品質指標

| 指標 | 台灣參考值 | 目標 |
|------|-----------|------|
| FDA 藥品總數 | 71,552 | 記錄 |
| 有效藥品比例 | 33% | > 20% |
| DrugBank 映射率 | 73.87% | > 50% |
| 疾病映射率 | 44.85% | > 30% |
| 預測候選數 | 142,328 | 記錄 |

**品質檢查點**：
- [ ] 端對端流程通過
- [ ] GitHub Pages 部署成功
- [ ] SMART App 可從 SMART Launcher 啟動

---

## 三、關鍵檔案詳解

### 3.1 `config/fields.yaml`

欄位映射設定檔，定義藥監局資料欄位與標準欄位的對應關係。

### 3.2 `src/txgnn/data/loader.py`

資料載入器，根據 `fields.yaml` 載入並過濾藥品資料。

### 3.3 `src/txgnn/mapping/disease_mapper.py`

疾病映射模組，包含 `DISEASE_DICT`（當地語言→英文對照表）。

### 3.4 `scripts/process_fda_data.py`

資料處理腳本，將原始資料轉換為標準 JSON 格式。

---

## 四、GitHub Actions 設定

### 需設定的 Workflow：

| Workflow | 功能 | 需修改 |
|----------|------|--------|
| `pages.yml` | Jekyll 部署 | URL |
| `link-check.yml` | 連結檢查 | 無 |
| `check-new-evidence.yml` | 證據檢查 | 無 |

### 需設定的 Secrets：

| Secret | 用途 |
|--------|------|
| `GITHUB_TOKEN` | 自動提供 |
| `NCBI_API_KEY` | PubMed API（可選，提高速率限制） |

---

## 五、驗證清單

### 總體完成檢查

- [ ] Phase 0：專案初始化完成
- [ ] Phase 1：FDA 資料整合完成
- [ ] Phase 2：疾病映射完成
- [ ] Phase 3：KG 預測完成
- [ ] Phase 4：網站與 FHIR 完成
- [ ] Phase 5：證據收集完成
- [ ] Phase 6：新聞監測完成
- [ ] Phase 7：驗證與部署完成

### YMYL 檢查（醫療內容必檢）

- [ ] 免責聲明：「僅供研究參考，不構成醫療建議」
- [ ] 預測結果標註：「需經臨床驗證」
- [ ] 資料來源標註完整

---

## 六、附錄：區域特殊考量

### 日本 (PMDA)
- 資料格式：可能有 Shift-JIS 編碼
- 藥名：漢字/平假名/片假名混用
- 臨床試驗：JPRN (UMIN-CTR, JapicCTI, JMACCT)

### 韓國 (MFDS)
- 資料格式：UTF-8
- 藥名：韓文 + 英文音譯
- 臨床試驗：CRIS

### 泰國 (Thai FDA)
- 資料格式：UTF-8
- 藥名：泰文 + 英文
- 臨床試驗：TCTR

### 常見挑戰

1. **成分名稱變異**：同一藥物可能有不同鹽類形式
2. **品牌名映射**：當地品牌名需對應到國際名稱
3. **適應症文字解析**：不同語言的標點符號慣例不同
4. **日期格式**：各地區日期格式不同
5. **狀態碼**：有效/註銷的術語不同

---

## 常用命令

```bash
# 安裝依賴
uv sync

# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜預測
uv run python scripts/run_kg_prediction.py

# 生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 本地測試網站
cd docs && bundle exec jekyll serve

# 執行測試
uv run pytest tests/ -v
```

---

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節）。
本站是第一個試做站，規則與程式都在本 repo，頁面文字用英文、依據是 FDA（Drugs@FDA、NDC Directory、DailyMed）。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁「## Review Log」表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/ustxgnn/regulatory/page_format.py` | 頁首＝Quick Overview「Evidence Level」格的**第一個**等級（主預測）。Tw 是整格取最高，本站不同：本站的格常寫「L5 for rank 1; L4 for …」「L5 (… does not meet L3 criteria)」，取最高會錯誤升級（2026-11-12 實測 20 頁） |
| 撤回預測 | `src/ustxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `scripts/sync_license_tables.py`、`snapshots/us_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/ustxgnn/regulatory/licenses.py` | 程式表前後有 `<!-- licenses:begin/end -->` 標記；快照存程式表列、總數、本藥申請號、事實層；gate 依快照驗號碼歸屬、程式表、狀態列與張數列 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依成分重建刪句後（`scripts/license_rebuild_run.py` 會自動跑）或依 git 前後版本，把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證；本站證據包目前沒有仿單適應症文字，可比對 0 頁（程式照實回報） |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首＝主預測等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照 FDA 資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、license_rebuild_run.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（排程與重建會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31、11-05～06 依成分重建後直接刪掉的矛盾子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 1,243 筆紀錄（707 頁；其中 8 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁時，會保留舊頁的程式許可證區塊並重套紀錄，notes 裡的舊錯句會被紀錄再更正一次。
2026-11-12 正文張數對事實層再掃一次：19 頁 AI 依舊證據包寫的「全部有效」、有效／停止張數、無保留的整體張數跟事實層相反，照上面的慣例刪掉矛盾子句（`us-lic-20261112-*`；dexamethasone、lansoprazole 是 11-06 那筆同 id 重發、前版存 history）。
有保留的「At least N／N listed … may be partial」、狀態正確只是筆數取自舊清單的句子、涉及 OTC monograph／NDC listings 口徑的句子不動。

## 新資料查不到的申請號（2026-11-17）

2026-11-17 每週排程：證據包 25,465 張申請號，openFDA Drugs@FDA 全量檔涵蓋 99.5%，「新資料查不到」135 張（沒開 issue）。用戶要求確認實際狀態：
下載 FDA 的現行清單逐號比對（2026-11-17）——openFDA Drugs@FDA、fda.gov Drugs@FDA 全量檔（drugsatfda.zip）、NDC Directory（ndctext／ndc_excluded／ndc_unfinished 與 openFDA NDC）、Purple Book 2026-10 月檔。
- 135 張全是證據包裡來源標「NDC Directory (not in Drugs@FDA)」的號碼：91 張 BLA（CBER 的疫苗、免疫球蛋白、血液製劑、過敏原萃取、細胞與基因治療；openFDA Drugs@FDA 只收 CDER）、
  43 張 ANDA（多是 repackager 在 NDC 引用的舊號碼，fda.gov Drugs@FDA 全量檔也沒有，核准狀態查不到）、1 張 NDA（NDA206627 Hysingla ER：fda.gov Drugs@FDA 有、處方藥，openFDA 沒收）。
- 135 張都在 NDC Directory 現行成品列名（2026-11-16）上，NDC 列名不等於核准狀態，但沒有一張能證明已失效；Purple Book 有 87 張 BLA，85 張 Licensed（有 Rx 產品；其餘 4 張是大型過敏原 BLA，Purple Book 沒收，NDC 有現行列名）。
- 2 張 Purple Book 為許可撤銷：BLA125586 Andexxa（Revoked，兩個產品 Disc；NDC 仍有 0310-3200 列名）、BLA125324 Prevnar 13（Voluntarily Revoked；證據包 streptococcus_pneumoniae…，沒有藥物頁）。
- `scripts/license_adapter.py`：Drugs@FDA 沒有的申請號另查 Purple Book 最新月檔（全部 Revoked → status 加「 (License revoked in Purple Book)」，算註銷；有 Licensed 的 Rx／OTC 產品 → 有效）
  與 openFDA NDC（有現行成品列名 → 有效）；兩份都是選用，下載失敗就略過。三份都沒有的申請號照舊保留原狀態、列為查不到，不推定註銷（Drugs@FDA 不含 CBER、Purple Book 不含部分過敏原 BLA、NDC 列名不等於許可），所以沒有 confirmed_absent。
  OTC monograph 等沒有申請號的紀錄不受影響。`scripts/sync_license_tables.py` 的表格狀態對這種紀錄寫「License revoked in Purple Book」。
- andexanet_alfa：狀態列／張數列與許可證表由排程同步（Marketed 1 of 1 → Not marketed）；11-06 的 `us-lic-20261106-andexanet_alfa-1` 當時依 Drugs@FDA／NDC 刪掉「The product's license is also cancelled in the US」，
  其實與 Purple Book 相符，2026-11-17 同 id 重發成 annotate（前版存 history），還原原句並加註。依成分查過，沒有其他 andexanet alfa 產品。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 902 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Detailed mechanism of action data is not available in the data compiled for this report.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `us-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：「According to the … section of the FDA-approved prescribing information for <藥>: "…" ([DailyMed: …](…), label version …; accessed …)」（本站就是美國站，不寫「US」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 2026-11-19 結果：807 頁寫入紀錄（美國仿單 768、ChEMBL 39），95 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：同一成分有多份仿單時只取一份（排序如上），劑型可能跟頁面討論的產品不同（例如取到外用仿單）。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 12 筆紀錄、1 頁列待查；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）35 筆改成那句在節錄前（原文不改，只換順序）；同頁重複引用同一段節錄的 1 筆改成指向上方節錄的一句（附同一個來源連結）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Approved use: Not recorded in the local data」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：FDA 申請號（active；另列 OTC monograph／未核准 NDC 列名）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：abatacept「Approved use: Not recorded in the local data」→「In the US: 1 FDA application (1 active)」；2026-11-19 改了 555 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site UsTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 正文許可證張數改由程式維護（2026-11-24）

用戶 2026-11-24 決定（30 站「許可證張數與狀態不再每週過期」）：本站已有程式許可證表（`scripts/sync_license_tables.py`，2026-11-06 起），這次只做 B（正文張數程式改寫），不重做 A。
- B. `scripts/rewrite_license_counts.py`＋`src/ustxgnn/regulatory/count_prose.py`（照 Kr／My／Eu／Ca 移植，英文句型）：依快照事實層改寫句型明確的「N valid licences」「N FDA applications」「X of Y authorizations are valid」「All N … are valid」；
  本站口徑：total＝FDA 申請號數（NDA／ANDA／BLA），listed（沒有申請號的 NDC 列名）不算進 total——有列名產品的頁，總數接受 total 與 total＋listed、有效接受 valid 與 valid＋listed，要改時讀法不唯一就不改（ambiguous）。
  有保留（at least、may be partial…）、講證據包或查詢、相對數（further、other、also…）、劑型、複方、申請類別或品牌子集（generic、ANDA、NDA、BLA、大寫品名、申請號）、NDC 列名／OTC monograph／unapproved、其他國家、講表格顯示筆數（listed、shown、table、below…）、事實層總數 0 的頁不動；
  同一行有判斷不了的整行不動；單方張數、0 張、跨過 1（單複數）、both、「all／both … valid」而事實不符的不改、列進待查清單。不寫查核框；查核紀錄 replacement／anchor 所在的句子不改。
- 接上：`scripts/apply_drug_reviews.py`（非 --check）結尾先跑 `sync_license_tables.run()`（已有程式區塊的頁依證據包＋快照事實層重排，沒有 data/bundles 時不動），再跑改寫；
  `scripts/build_license_snapshot.py` 寫完快照後同樣先重排程式表（用 --ws 的事實層）再改寫（`--no-rewrite` 不跑；不給 --ws 時不重建快照、只跑這兩步，母目錄排程 3a' 用）；
  `scripts/license_rebuild_run.py` 轉紀錄前那次建快照加 `--no-rewrite`（免得改寫的張數被 reviews_from_edits 當成刪改）；gate 第 22 項（`scripts/check_seo_docs.py`）擋「再跑一次會變」。
  `scripts/reviews_from_edits.py` 的 figures() 不再寫當日張數（改成指向概覽表與程式許可證表）。
- 2026-11-24 套用（資料 data-20261123-183708）：公開藥物頁 953 頁（程式表 236 頁、AI 表 701 頁、段落沒有表 12 頁、沒有市場段落 4 頁）；改寫 0 句（AI 正文的張數句幾乎都帶「may be partial／at least」保留語，或講表上筆數；唯一一句 apixaban「Of the 5 licences listed, 3 are valid…」講的是表上 5 列、跟那 5 列一致，DISPLAY 加 bare「listed」後不改）；
  判斷不了 9 句列進待查清單（ambiguous 3、display 5、grammar 1）。
- 查核紀錄張數不寫死（用戶同日追加決定）：1,224 筆紀錄 note 裡「The FDA data list N FDA applications … N active」改成「The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information.」，同 id 重發、前版存 history（688 頁查核框文字跟著換，last_modified_at 不動）；
  `us-lic-20261106-zolmitriptan-1` 的 replacement 留下的舊表說明句「Only 5 of the 11 authorizations are shown.」（總數已是 26）一併刪掉。其他 replacement 裡的張數句都在 AI 表的頁、講的是那張表（例「Five representative licenses are listed below.」），不動。
- 單方／複方標籤：celecoxib「every record is listed as "single-ingredient" type」，證據包有 CONSENSI（NDA210045）、SEGLENTIS（NDA213426）2 筆複方，以 `us-lic-20261124-celecoxib-1` 更正；其他「single-ingredient」句講的是表上列出的產品或帶保留語，逐句對過沒有相反的。
- 另寫的寬偵測（同句有許可字樣、數字不在事實層任一讀法或表格列數）全量掃公開頁：改前 117 句、改後 114 句。找到 3 頁只有 NDC 列名（total 0，程式不改）卻寫「all three US products are cancelled」「Neither of the two US licences is currently valid」「Both US products are also cancelled」，
  事實層列名 42／247／180 筆現行，以 `us-lic-20261124-{aluminum_chloride-1,-2,sennosides-1,stannous_fluoride-1}` 刪掉矛盾子句。剩 114 句：保留語 40、講表上筆數 37、子集 13、相對數 11、單方 4、其他 9（多是 AI 表的說明句、交互作用筆數、非許可證數字）。
- 還沒做：701 頁公開頁的市場段落仍是 AI 寫的自由格式許可證表（只有 236 頁是程式表），表上的「(cancelled)」狀態字與表下說明句會跟事實不一致（例 sennosides、aluminum_chloride 的列名產品寫成 cancelled）；要不要對這些頁做 A 待用戶決定。
  母目錄 `.claude/license_labels/UsTxGNN.json` 只有「Valid」，程式表另會寫「Discontinued in Drugs@FDA」「License revoked in Purple Book」（cancelled）；排程的狀態格同步會把這兩種列成 unsynced（程式表本身由 sync_tables／build_license_snapshot 重排，不受影響）。

## 市場段落 AI 許可證表全部換成程式表、舊錯句逐句更正（2026-11-24 第二輪）

用戶 2026-11-24 第二輪決定：第一輪後仍有 701 個公開頁（＋noindex 1 頁）的市場段落是模型寫的自由格式許可證表（表頭 Authorization Number…／Licence…，程式表只有 236 頁），
其中有把列名產品寫成 cancelled 的舊表（sennosides、aluminum_chloride 等），每週排程只改得到概覽表。
- `scripts/sync_license_tables.py --migrate --ws <工作目錄>`：市場段落第一張 AI 許可證表換成程式表（列數＝原表列數與 min(5, 總數) 取大、最多 20，同 render），702 頁；
  段落裡沒有表、證據包有紀錄的公開頁在段落第一段後補程式表，12 頁；緊鄰舊表、只講「清單可能不完整」的句子（CAPTION_P）與段落內只講舊表／下表列了幾筆的句子（CAPTION_D）拿掉 68 句；
  ferumoxytol 段落裡重複的第二張 AI 表一併拿掉。查核紀錄的更正文字與錨點所在的句子不動。錨在舊表列上的查核紀錄 0 筆（不用標 superseded，supersede() 照 FR 慣例留著）。
- gate（`src/ustxgnn/regulatory/licenses.py`）加一條：市場段落（程式區塊外）不准再有模型寫的許可證表。
- 換表後另寫一支更寬的獨立偵測（市場段落講張數、全稱狀態、顯示筆數、劑型全稱的句子，對事實層與證據包全部紀錄的劑型）全量掃公開頁：207 句（174 頁）。
  逐句對照後以 89 筆 `us-lic-20261124b-*` 更正（張數改成不寫數字、講舊表「另外 N 張／第六張／not shown」的句子刪、劑型全稱改成成立的寫法：例 celecoxib「The licences are for oral capsules」→「Most licences …」（另有錠劑、懸液、溶液）、
  mitomycin「only as an injectable」、doxycycline「All products are oral」、mometasone「All are metered nasal sprays」、diazoxide「Only an oral suspension」；沒有 FDA 申請號、只有 NDC 列名的頁寫成「唯一一張有效／已註銷」的改正前提：deanol、hyoscyamine、povidone、aluminum_oxide），
  更正文字本身是舊表說明或寫死張數的 20 筆 11-05～11-12 紀錄同 id 重發（前版存 history；dasatinib-1 改錨）；直接拿掉只講下表列了幾筆的說明句 16 句。市場段落外另掃「only … form／The only … licence」句 63 句，5 句不成立以紀錄更正。
  待查清單 11-24 新增的 9 句全部標 resolved（7 句寫紀錄，mitomycin、nystatin 的表說明句在換表時拿掉）。
- 寬偵測複查剩 123 句：劑型說法 76 句（逐句對照證據包都成立，或是不排他的列舉）、「at least N」保留語且 N 不大於事實層總數的句子、狀態全稱與事實一致的句子；沒有跟事實相反、未處理的句子。
  checker 全量前後都是 0；gate exit 0；改到的頁 last_modified_at 改 2026-11-24。
