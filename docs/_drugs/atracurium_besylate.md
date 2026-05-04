---
layout: default
title: Atracurium Besylate
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Atracurium Besylate
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

Using `txgnn-pipeline` to generate this drug repurposing evaluation report. Now producing the report based on the Evidence Pack.

---

# Atracurium Besylate: From Surgical Neuromuscular Blockade to Preeclampsia

## One-Sentence Summary

Atracurium besylate is a non-depolarizing neuromuscular blocking agent (NMBA) used as an adjunct to general anesthesia, providing skeletal muscle relaxation to facilitate endotracheal intubation and surgical procedures.
The TxGNN model predicts a potential association with **Preeclampsia**, with **0 clinical trials** and **4 publications** retrieved.
However, a critical review reveals that all available evidence reflects the use of atracurium as an **anesthetic agent in patients who happen to have preeclampsia**, not as a treatment for the condition — suggesting this prediction is a knowledge graph co-occurrence artifact rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neuromuscular blockade in general anesthesia (no Taiwan regulatory record available) |
| Predicted New Indication | Preeclampsia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, atracurium besylate is a benzylisoquinolinium non-depolarizing NMBA that competitively and reversibly blocks nicotinic acetylcholine receptors (N₂) at the skeletal muscle neuromuscular junction, producing dose-dependent muscle paralysis. A key distinguishing property is **Hofmann elimination** — a spontaneous, non-enzymatic chemical degradation dependent on physiological pH and temperature, independent of hepatic or renal function — which makes it particularly suitable for patients with multiorgan compromise.

The predicted connection to preeclampsia does **not** reflect a therapeutic mechanism. The knowledge graph association arises because pre-eclamptic patients undergoing cesarean section under general anesthesia routinely receive atracurium as a standard muscle relaxant component of the anesthetic regimen. The most direct reference, PMID 3778800 (1986), evaluated the *pharmacodynamic behavior* of atracurium within pre-eclamptic patients — observing that neuromuscular block duration may be slightly prolonged due to altered physiology — but this is a drug safety assessment, not a therapeutic efficacy study.

In summary, the TxGNN score of 99.97% for preeclampsia is almost certainly a **false positive driven by anesthetic co-occurrence** in the training graph. Atracurium causes whole-body skeletal muscle paralysis requiring mechanical ventilation; systemic NMBA administration is physiologically incompatible with the outpatient or conservative management that preeclampsia typically requires. There is no established or theoretically plausible mechanism by which atracurium would treat the hypertensive or endothelial pathophysiology of preeclampsia.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for atracurium besylate in preeclampsia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3778800](https://pubmed.ncbi.nlm.nih.gov/3778800/) | 1986 | Observational / Case Series | British Journal of Anaesthesia | Evaluated pharmacodynamics of atracurium in pre-eclamptic patients; NMB duration may be slightly prolonged; anesthetic safety study, not treatment efficacy |
| [9646009](https://pubmed.ncbi.nlm.nih.gov/9646009/) | 1998 | Pharmacokinetic Review | Clinical Pharmacokinetics | PK of NMBAs (atracurium, vecuronium, pancuronium) during pregnancy; Vss and clearance of atracurium unchanged despite plasma volume expansion |
| [18383970](https://pubmed.ncbi.nlm.nih.gov/18383970/) | 2008 | Case Series | Rev Esp Anestesiol Reanim | Remifentanil for hemodynamic control in high-risk C-sections ineligible for spinal anesthesia; atracurium used as standard GA adjunct, unrelated to preeclampsia treatment |
| [41103680](https://pubmed.ncbi.nlm.nih.gov/41103680/) | 2025 | RCT | Anesthesiology and Pain Medicine | Inflammatory cytokines (IL-6, leptin, adiponectin) compared after C-section under GA vs spinal; atracurium part of GA protocol, not the study intervention |

> ⚠️ **Note**: None of these studies test atracurium as a treatment *for* preeclampsia. All four involve atracurium as a routine anesthetic component in obstetric or high-risk surgical settings. The evidence does not support repurposing.

---

## Taiwan Market Information

Atracurium besylate has **no registered products** in Taiwan's drug database (TFDA query returned 0 records). There are no approved NDAs or import licenses on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers**: TFDA package insert warnings and contraindications could not be retrieved (Data Gap DG001, severity: Blocking). Key safety concerns known from general pharmacology include: respiratory arrest requiring mechanical ventilation, histamine release (risk of bronchospasm and hypotension), and accumulation of the CNS-active metabolite **laudanosine** in patients with hepatic failure or prolonged infusion — the latter carries seizure risk. These should be formally verified before any clinical use assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction linking atracurium besylate to preeclampsia is mechanistically unfounded — the knowledge graph connection is a co-occurrence artifact from anesthetic use in obstetric surgery, not a therapeutic signal. A systemic NMBA that causes whole-body paralysis and requires ventilatory support cannot plausibly serve as a treatment for a hypertensive disorder of pregnancy. All retrieved literature confirms anesthetic context only.

**To proceed, the following is needed:**

- Confirm and document the formal original indication (surgical neuromuscular blockade) from a regulatory source (e.g., FDA label, WHO INN monograph)
- Retrieve MOA data from DrugBank (DB00732) to complete mechanistic documentation (Data Gap DG002)
- Obtain and parse the TFDA package insert PDF for safety warnings and contraindications (Data Gap DG001, currently Blocking)
- Consider flagging this candidate as a **known graph artifact** in the TxGNN pipeline to prevent repeated false-positive generation for anesthetic agents in disease co-occurrence settings
- No further clinical evidence collection is recommended unless a novel mechanism hypothesis is proposed and peer-reviewed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

