---
layout: default
title: Danazol
parent: 僅模型預測 (L5)
nav_order: 567
evidence_level: L5
indication_count: 10
---

# Danazol
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

# Danazol: From Endometriosis to Amenorrhea

## One-Sentence Summary

Danazol is a synthetic steroid derived from 17α-ethinyltestosterone, with US FDA approval for endometriosis, fibrocystic breast disease, and hereditary angioedema, though it is not registered in the Taiwan market.
The TxGNN model predicts it may be clinically relevant for **Amenorrhea (disease)**, supported by **0 registered clinical trials** and **20 publications** — primarily capturing amenorrhea as a known pharmacological outcome of Danazol treatment.
**Important clinical nuance**: Danazol is known to **induce** amenorrhea as a therapeutic mechanism (used in endometriosis and menstrual suppression), rather than treating pathological primary amenorrhea; this distinction is critical for interpreting the prediction's clinical applicability.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; US FDA approved for Endometriosis, Fibrocystic Breast Disease, Hereditary Angioedema (per PMID 39051650) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.9995% |
| Evidence Level | L3 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Registered Licenses (Taiwan) | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism of action (MOA) data from DrugBank was not available in this Evidence Pack, but the published literature provides a clear mechanistic picture. Danazol is a synthetic steroid with multiple and diverse biological effects: it centrally inhibits pituitary FSH and LH secretion, thereby suppressing ovarian gametogenesis and steroidogenesis; it binds steroid transport proteins (such as SHBG and CBG) in circulation and to specific receptors in target tissues; and it directly suppresses gonadal and adrenal steroidogenesis through effects on specific enzyme systems (PMID 2404115). The net result is a hypoestrogenic, anovulatory state in which amenorrhea is the expected and intended therapeutic outcome.

In the context of endometriosis, this amenorrheic state is the mechanism of action — endometrial lesions regress under ovarian down-regulation, as they depend on cyclical estrogen stimulation and menstrual-like bleeding for proliferation (PMID 16280355). The prediction therefore reflects a genuine and well-established drug–disease relationship in the knowledge graph: Danazol reliably induces amenorrhea. A 2024 multi-site retrospective cohort study (PMID 39051650) further documented this mechanism in a newer clinical context — menstrual suppression in transgender and non-binary individuals — confirming the pharmacological effect extends beyond the classic endometriosis indication.

**⚠️ Conceptual Distinction**: TxGNN labels this as a disease entity ("amenorrhea as disease"), whereas Danazol's role is to **induce** amenorrhea therapeutically. Primary or pathological amenorrhea (e.g., hypothalamic, pituitary, or gonadal failure) would require a completely different therapeutic approach. The clinical value of this prediction lies in formalizing "therapeutic amenorrhea induction" (menstrual suppression) as an explicit indication — particularly relevant for emerging gender-affirming care applications — rather than in treating spontaneous amenorrhea.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the specific indication "amenorrhea (disease)."

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2140996](https://pubmed.ncbi.nlm.nih.gov/2140996/) | 1990 | RCT | Fertility and Sterility | Double-blind RCT (n=82): nafarelin 400 µg/day vs danazol 600 mg/day for 6 months in endometriosis; both caused significant active lesion regression with amenorrhea as a primary treatment endpoint; no difference in efficacy between arms |
| [36434439](https://pubmed.ncbi.nlm.nih.gov/36434439/) | 2023 | Systematic Review | Archives of Gynecology and Obstetrics | Meta-analysis comparing gestrinone vs danazol in endometriosis; gestrinone induces amenorrhea comparably to danazol with a more favorable androgenic side-effect profile |
| [39051650](https://pubmed.ncbi.nlm.nih.gov/39051650/) | 2024 | Retrospective Cohort | Women's Health | Multi-site retrospective cohort: danazol used for menstrual suppression in transgender and non-binary individuals; effective at inducing amenorrhea, with reversible androgenic effects (voice changes, hair pigmentation) valued by some patients |
| [6819580](https://pubmed.ncbi.nlm.nih.gov/6819580/) | 1982 | Clinical Study | Progress in Clinical and Biological Research | Danazol suppresses ovarian function via gonadotropin inhibition; treatment of endometriosis-associated infertility by inducing a hypoestrogenic, amenorrheic state significantly improves conception rates |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Clinical Review | Journal of the Royal Army Medical Corps | Survey of therapeutic amenorrhea induction methods (OCP, GnRH analogues, danazol) for clinical menstrual suppression; danazol noted as an effective but potentially androgenic option |
| [2404115](https://pubmed.ncbi.nlm.nih.gov/2404115/) | 1990 | Review | Journal of Reproductive Medicine | Comprehensive mechanistic review: Danazol inhibits gonadotropins, suppresses steroidogenesis through specific enzyme systems, and modulates immunological responses — the integrated effect of which induces a reliable amenorrheic state |
| [16280355](https://pubmed.ncbi.nlm.nih.gov/16280355/) | 2006 | Review | Human Reproduction Update | Endometriosis management update: lesion regression occurs during ovarian down-regulation states (amenorrhea, menopause); amenorrhea is both the mechanism and the biomarker of treatment success |
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | Evidence-based review of pharmacological therapies for abnormal uterine bleeding; danazol included as an agent that reduces or eliminates bleeding by suppressing the hypothalamic–pituitary–ovarian axis |
| [1807260](https://pubmed.ncbi.nlm.nih.gov/1807260/) | 1991 | Case Series | Asian Pacific Journal of Allergy and Immunology | Seven SLE patients with refractory thrombocytopenia treated with danazol; 4/5 completers achieved complete response — highlighting immunomodulatory applications beyond gynecology |
| [2013670](https://pubmed.ncbi.nlm.nih.gov/2013670/) | 1991 | Cohort Study | Journal of Allergy and Clinical Immunology | 56 hereditary angioedema patients on long-term attenuated androgen prophylaxis (danazol ≤200 mg/day or stanozolol ≤2 mg/day) for >5 years; irregular menstruation noted as a frequent side effect, confirming dose-dependent ovarian suppression |

---

## US Market Information

Danazol is not registered in the Taiwan TFDA database (0 approved licenses). No Taiwan-specific product or indication data is available.

Based on literature evidence, Danazol holds US FDA approval for the following indications:

| Approved Indication | Supporting Literature |
|--------------------|-----------------------|
| Endometriosis | PMID 39051650, 6819580, 2140996 |
| Benign Fibrocystic Breast Disease | PMID 39051650, 7041729 |
| Hereditary Angioedema | PMID 39051650, 2013670 |

> Formal US NDA numbers were not available in this Evidence Pack. For official authorization details, refer to [FDA Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/).

---

## Safety Considerations

Formal safety data (TFDA package insert warnings and contraindications) were not retrieved in this Evidence Pack. The following safety signals are identified from available literature:

- **Androgenic Side Effects**: Danazol carries dose-dependent androgenic effects including acne, oily skin, hirsutism, voice changes, and weight gain (PMID 39051650, 2404115).
- **Lactation Contraindication**: Danazol is contraindicated during breastfeeding due to risk of androgenic exposure in nursing infants (PMID 36744397).
- **Statin Interaction (DDI)**: Co-administration of danazol 600 mg/day with lovastatin 40 mg/day has been reported to cause rhabdomyolysis and pancreatitis, likely through CYP3A4 inhibition by danazol (PMID 18691993). Caution with statin co-prescription is warranted.
- **Pregnancy**: Contraindicated in pregnancy due to risk of fetal androgenization (consistent across multiple sources).

Please refer to the official package insert for complete safety, contraindication, and monitoring information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for amenorrhea reflects a well-characterized and clinically utilized pharmacological property of Danazol — its reliable ability to induce amenorrhea through hypothalamic–pituitary–ovarian axis suppression. Rather than a speculative repurposing, this represents an opportunity to formalize an already-occurring clinical application (particularly menstrual suppression in gender-affirming care, as documented in PMID 39051650) under a structured regulatory and safety framework. The L3 evidence base (observational studies, systematic reviews, retrospective cohort) is sufficient to support a "Proceed with Guardrails" position for further clinical characterization.

**To proceed, the following is needed:**
- Retrieve MOA documentation from DrugBank (Data Gap DG002: High severity) to support mechanistic analysis and repurposing rationale
- Retrieve Taiwan TFDA package insert for complete contraindication, warning, and dosage guidance (Data Gap DG001: Blocking — required before safety evaluation)
- Clarify the clinical target population: "therapeutic amenorrhea induction" (e.g., endometriosis, gender-affirming care, menstrual suppression) is a viable indication pathway; treatment of primary pathological amenorrhea is not supported and should be explicitly excluded from scope
- Conduct a prospective clinical study or registry-based study specifically for menstrual suppression as a primary endpoint, as no registered clinical trials currently address this specific indication
- Verify current US NDA scope via FDA Drugs@FDA to assess whether new indication filing or label expansion is required for the menstrual suppression use case
- Review Taiwan regulatory pathway for re-registration, given current zero-license status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

