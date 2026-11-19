---
layout: default
title: About
nav_order: 90
permalink: /about/
last_modified_at: 2026-11-04
description: "UsTxGNN is a drug repurposing prediction platform developed by 藥提醒科技有限公司 (yao.care), built on the Harvard TxGNN model, covering FDA-approved medicines in United States."
---

# About

<div class="key-takeaway">
Accelerating drug repurposing evidence validation with AI — from prediction to evidence at a glance.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## United States: this site's data in numbers

Local data: [FDA National Drug Code Directory](https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory). The local data are FDA application numbers from Drugs@FDA, with the NDC Directory and the Purple Book for products that Drugs@FDA does not cover. An application whose products are all discontinued, or whose licence the Purple Book lists as revoked, is not counted as marketed.

| Item | Value |
|---|---|
| Medicines with a published report | {{ site.data.local_facts.drugs_total }} |
| Medicines found in the local data | {{ site.data.local_facts.licence.drugs_with_data }} |
| …with at least one marketed entry | {{ site.data.local_facts.licence.drugs_with_current }} |
| …with entries but none marketed | {{ site.data.local_facts.licence.drugs_none_current }} |
| Medicines not in the local data | {{ site.data.local_facts.licence.drugs_without_data }} |
| Local entries (FDA applications (NDA/ANDA/BLA)) | {{ site.data.local_facts.licence.items_total }} |
| …of which marketed | {{ site.data.local_facts.licence.items_current }} |
| Review-log entries | {{ site.data.local_facts.reviews.records }} |
| Drug pages with review-log entries | {{ site.data.local_facts.reviews.public_pages_with_records }} |
| Predicted drug–disease pairs found on no other TxGNN site | {{ site.data.local_facts.cross.unique_pairs }} |

{% if site.data.local_facts.top_licensed.size > 0 %}Medicines with the most marketed FDA applications (NDA/ANDA/BLA): {% for r in site.data.local_facts.top_licensed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Latest review-log corrections: {% for r in site.data.local_facts.recent_reviews limit: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

Examples of predictions that no other TxGNN site lists for the same medicine: [Platinum]({{ '/drugs/platinum/' | relative_url }}) → urinary bladder carcinoma, [Alosetron]({{ '/drugs/alosetron/' | relative_url }}) → migraine disorder, [Ammonia N-13]({{ '/drugs/ammonia-n-13/' | relative_url }}) → non-syndromic esophageal malformation, [Amphetamine]({{ '/drugs/amphetamine/' | relative_url }}) → faciodigitogenital syndrome, [Aripiprazole Lauroxil]({{ '/drugs/aripiprazole-lauroxil/' | relative_url }}) → retinal dystrophy with or without extraocular anomalies, [Benzphetamine]({{ '/drugs/benzphetamine/' | relative_url }}) → hypervitaminosis, [Binetrakin]({{ '/drugs/binetrakin/' | relative_url }}) → craniostenosis cataract, [Black Cohosh]({{ '/drugs/black-cohosh/' | relative_url }}) → heart disease.

<!-- local-facts:end -->

## Background

<p class="key-answer" data-question="What is UsTxGNN?">
<strong>UsTxGNN</strong> is a research-support platform for drug repurposing, built on the TxGNN
model published in <em>Nature Medicine</em> by the Zitnik Lab at Harvard University. It predicts
indication expansion for medicines approved by FDA in United States. Beyond AI prediction scores,
the platform integrates clinical evidence from ClinicalTrials.gov and PubMed so researchers can
quickly assess how credible each prediction is.
</p>

---

<!-- local-condensed:start（母目錄 .claude/gen_local_pages_20261119.py；原共用段落縮寫，勿手改）-->
## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care, company registration number 83620786, Taichung City, Taiwan) as one of 30 country and region sites of its TxGNN drug repurposing product line ([product overview](https://www.yao.care/medical/txgnn/)).

---

## Method in brief

Predictions come from TxGNN, a graph neural network model from the Zitnik Lab at Harvard Medical School (Huang et al., *Nature Medicine* 2024, [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)); each predicted indication is graded L1–L5 against ClinicalTrials.gov and PubMed. Model, evidence levels and grading rules: [Methodology]({{ '/methodology/' | relative_url }}). Datasets, download links and licences: [Data Sources]({{ '/sources/' | relative_url }}).
<!-- local-condensed:end -->

---

## Contact

- **GitHub Issues**: <https://github.com/yao-care/UsTxGNN/issues>
- **Developer**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Product overview**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research reference only and <strong>does not constitute medical advice</strong>. Always follow your physician's instructions; never adjust medication on your own. Any drug repurposing decision requires full clinical validation and regulatory review.
<br><br>
<small>Reviewed by: 藥提醒科技有限公司 (yao.care)</small>
</div>
