---
layout: default
title: Collagenase Clostridium Histolyticum
parent: 僅模型預測 (L5)
nav_order: 548
evidence_level: L5
indication_count: 10
---

# Collagenase Clostridium Histolyticum
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Collagenase Clostridium Histolyticum: From Dupuytren's Contracture to Ledderhose Disease

## One-Sentence Summary

Collagenase Clostridium Histolyticum (CCH) is a bacterial collagenase enzyme recognized internationally for treating Dupuytren's contracture (palmar fibromatosis), though no US market licenses were retrieved in this database query.
The TxGNN model predicts it may also be effective for **Ledderhose disease** (plantar fibromatosis), supported by **3 published case reports** and an indirect clinical trial in the same fibromatosis family.
Separately, the model identified **palmar fibromatosis** (Dupuytren's contracture) as a high-confidence secondary prediction — supported by **32 clinical trials** and **20 publications** — consistent with CCH's globally established mechanism.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Dupuytren's Contracture (palmar fibromatosis; internationally recognized use, no license found in database) |
| Predicted New Indication | Ledderhose Disease (plantar fibromatosis) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (case reports for Ledderhose; mechanistically linked palmar fibromatosis shows L1) |
| US Market Status | 未上市 (0 licenses found — see note below) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

> ⚠️ **Database Note**: The data pipeline returned 0 US records for CCH. However, CCH (Xiaflex®) is known to have received FDA approval for Dupuytren's contracture in 2010 and Peyronie's disease in 2013. This likely reflects a data retrieval gap. Verify via FDA Orange Book before making regulatory decisions.

---

## Why is This Prediction Reasonable?

CCH consists of two highly selective bacterial collagenases (AUX-I and AUX-II) derived from *Clostridium histolyticum*, which specifically degrade types I and III collagen — the dominant structural proteins in pathological fibrous cords. In Dupuytren's contracture, CCH disrupts the collagen-rich cords that form in the palmar fascia, allowing passive finger extension and restoring hand function without surgery.

Ledderhose disease (plantar fibromatosis) is a fibroproliferative disorder of the plantar fascia that shares nearly identical histopathology with Dupuytren's contracture: abnormal myofibroblast proliferation, excessive type I and III collagen deposition, and formation of fibrotic nodules within fascial tissue. The critical difference is only anatomical — plantar (foot sole) versus palmar (hand palm). Since the collagen composition of pathological cords is the same in both conditions, CCH's enzymatic mechanism should be equally applicable to plantar fibromatosis nodules.

Published case reports (see Literature Evidence) have already demonstrated that off-label CCH injection can reduce plantar fibromatosis nodule size with favorable short-term outcomes. Furthermore, CCH has proven efficacy in Peyronie's disease (penile fibromatosis) — a third fibromatosis condition — reinforcing that CCH's mechanism generalizes across anatomically distinct fibroproliferative disorders. TxGNN's prediction aligns directly with this mechanistic logic.

---

## Clinical Trial Evidence

### Ledderhose Disease (Direct Search Results)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01184586](https://clinicaltrials.gov/study/NCT01184586) | Phase 2 | Unknown | 60 | Extracorporeal shockwave therapy for Dupuytren's disease nodules — returned in Ledderhose search as a related fascial fibromatosis study; not a direct CCH+Ledderhose trial |

> No dedicated CCH clinical trials specifically for Ledderhose disease are currently registered on ClinicalTrials.gov.

### Palmar Fibromatosis / Dupuytren's Contracture (Mechanistically Linked Evidence)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00528606](https://clinicaltrials.gov/study/NCT00528606) | Phase 3 | Completed | 308 | Pivotal US double-blind RCT: CCH 0.58 mg vs placebo for Dupuytren's contracture (MP and PIP joints) |
| [NCT00533273](https://clinicaltrials.gov/study/NCT00533273) | Phase 3 | Completed | 66 | Phase 3 double-blind RCT + open-label extension for advanced Dupuytren's disease |
| [NCT00528840](https://clinicaltrials.gov/study/NCT00528840) | Phase 3 | Completed | 201 | Open-label Phase 3 safety and efficacy for advanced Dupuytren's disease over 9 months |
| [NCT01588353](https://clinicaltrials.gov/study/NCT01588353) | Phase 3 | Completed | 104 | Japanese Phase 3 study (AK160/CCH) in Dupuytren's contracture |
| [NCT02725528](https://clinicaltrials.gov/study/NCT02725528) | Phase 3 | Completed | 22 | Multi-center RCT: CCH (Xiaflex) vs palmar fasciectomy — clinical effectiveness and cost-effectiveness |
| [NCT04874870](https://clinicaltrials.gov/study/NCT04874870) | Phase 3 | Completed | 80 | RCT: splinting vs no splinting after CCH injection for Dupuytren's contracture |
| [NCT01674634](https://clinicaltrials.gov/study/NCT01674634) | Phase 3 | Completed | 715 | Concurrent dual CCH injections into same hand — large safety study (N=715) |
| [NCT00528424](https://clinicaltrials.gov/study/NCT00528424) | Phase 3 | Completed | 286 | Open-label extension: repeated CCH injections across multiple cord-affected joints |
| [NCT01229436](https://clinicaltrials.gov/study/NCT01229436) | Phase 3 | Completed | 254 | Prospective open-label real-world study of CCH (Xiapex) — ROM, satisfaction, and recovery time |
| [NCT03192020](https://clinicaltrials.gov/study/NCT03192020) | Phase 4 | Active, not recruiting | 302 | DETECT trial: head-to-head RCT comparing CCH vs needle fasciotomy vs surgery as primary strategies |

---

## Literature Evidence

### Ledderhose Disease (Direct Evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [25158740](https://pubmed.ncbi.nlm.nih.gov/25158740/) | 2014 | Case Report | Plastic and Reconstructive Surgery | First published report of CCH injection for plantar fibromatosis (Ledderhose disease) |
| [31679681](https://pubmed.ncbi.nlm.nih.gov/31679681/) | 2019 | Case Study | Journal of Foot and Ankle Surgery | CCH effects on plantar fibromatosis; notes high surgical recurrence rates and nerve injury risks as rationale for CCH use |
| [37869482](https://pubmed.ncbi.nlm.nih.gov/37869482/) | 2023 | Case Report | Foot & Ankle Orthopaedics | Ultrasound-guided CCH injection for recurrent plantar fibromatosis — supports image-guided delivery technique |

### Palmar Fibromatosis / Dupuytren's Contracture (Mechanistically Linked Evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39383454](https://pubmed.ncbi.nlm.nih.gov/39383454/) | 2024 | RCT | New England Journal of Medicine | Landmark NEJM comparison: CCH injection vs limited fasciectomy for Dupuytren's contracture |
| [37665353](https://pubmed.ncbi.nlm.nih.gov/37665353/) | 2024 | Meta-Analysis | Archives of Orthopaedic and Trauma Surgery | Systematic review and meta-analysis of CCH vs limited fasciectomy for Dupuytren's disease |
| [26524616](https://pubmed.ncbi.nlm.nih.gov/26524616/) | 2015 | Systematic Review | Health Technology Assessment | HTA systematic review and economic evaluation of CCH for Dupuytren's contracture |
| [32484064](https://pubmed.ncbi.nlm.nih.gov/32484064/) | 2020 | Meta-Analysis | Journal of Orthopaedic Surgery (Hong Kong) | Meta-analysis: efficacy and limitations of CCH vs fasciectomy; treatment algorithm |
| [27050718](https://pubmed.ncbi.nlm.nih.gov/27050718/) | 2016 | Review | Journal of Plastic Surgery and Hand Surgery | Comprehensive review of CCH: emerging practice patterns and advances across fibromatosis indications |
| [27151958](https://pubmed.ncbi.nlm.nih.gov/27151958/) | 2016 | Systematic Review | British Medical Bulletin | Systematic review of CCH in Dupuytren's contracture: procedure safety and outcomes |
| [26491251](https://pubmed.ncbi.nlm.nih.gov/26491251/) | 2015 | Review | Biologics: Targets & Therapy | CCH in Peyronie's disease — demonstrates efficacy across a third anatomically distinct fibromatosis condition |
| [24698851](https://pubmed.ncbi.nlm.nih.gov/24698851/) | 2015 | Comparative Study | Journal of Hand Surgery, European Volume | Safety comparison: CCH (N=1,082 across 11 trials) vs fasciectomy (N=7,727); CCH showed lower nerve injury and complication rates |
| [30676501](https://pubmed.ncbi.nlm.nih.gov/30676501/) | 2019 | Clinical Study | Plastic and Reconstructive Surgery | Single vs concurrent CCH injections for Dupuytren's — FDA approved concurrent use in 2014 |
| [40047775](https://pubmed.ncbi.nlm.nih.gov/40047775/) | 2025 | Clinical Study | Journal of Hand Surgery | Orthosis effectiveness after CCH injection — post-treatment rehabilitation optimization |

---

## Safety Considerations

No safety data was retrieved from the database for this drug. Please refer to the package insert for full safety information.

Based on published clinical literature, the following safety signals are documented:

- **Local site reactions**: Swelling, ecchymosis, pain, and tenderness at injection site are extremely common (>90% in clinical trials) but typically resolve within 1–2 weeks
- **Skin laceration**: Spontaneous skin tears during manual extension maneuver reported; risk management requires careful technique (PMID 29570549)
- **Tendon rupture / ligament injury**: Rare but serious; reported in Phase 3 trials and post-marketing surveillance
- **Antithrombotic drug interaction**: A dedicated study (PMID 34789118, N=148) found no significant increase in complications for patients on antithrombotic therapy, though bruising may be more pronounced

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
CCH's mechanism of collagen I/III degradation is directly relevant to Ledderhose disease, which shares identical fibroproliferative pathology with Dupuytren's contracture at a different anatomical site. Published case reports confirm clinical feasibility, and the drug's extensive Phase 3 safety and efficacy data from Dupuytren's and Peyronie's disease provides a strong mechanistic and safety foundation for clinical translation to plantar fibromatosis.

**To proceed, the following is needed:**

- **Dedicated clinical trial**: A prospective Phase 2 trial of CCH specifically for Ledderhose disease is the critical next step — no such trial currently exists
- **Dosing and delivery optimization**: The plantar fascia differs anatomically from the palmar fascia; injection depth, volume, and manipulation technique require adaptation and formal study
- **US regulatory database verification**: Confirm whether CCH (Xiaflex®) holds current FDA approval — the database returned 0 records, which is likely a data pipeline issue given known FDA approval history
- **MOA documentation**: Formal mechanism of action data is marked as a data gap in this Evidence Pack; complete this for regulatory submissions
- **Safety assessment for plantar route**: Post-injection weight-bearing restrictions, footwear accommodations, and recurrence monitoring protocols are needed

---

> **⚠️ False Positive Alert — Ranked Predictions #1–3, #7–9**: The TxGNN model scored several platelet and coagulation disorders (primary release disorder of platelets, Glanzmann thrombasthenia, pseudo-von Willebrand disease, hemorrhagic disorder due to constitutional thrombocytopenia, Scott syndrome) with high scores. These predictions are mechanistically implausible — CCH degrades extracellular collagen and has no known pathway to platelet granule secretion, GPIIb/IIIa function, or phospholipid membrane asymmetry. They are assessed as model false positives arising from indirect knowledge graph links between collagen and platelet activation. **Prediction #9 (bleeding diathesis due to collagen receptor defect) warrants particular caution**: CCH degrades the collagen substrate that platelet receptors bind to, which could theoretically worsen bleeding in this population rather than treat it. None of these platelet/coagulation predictions should be advanced.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

