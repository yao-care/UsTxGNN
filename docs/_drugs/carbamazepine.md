---
layout: default
title: Carbamazepine
parent: 僅模型預測 (L5)
nav_order: 495
evidence_level: L5
indication_count: 10
---

# Carbamazepine
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

# Carbamazepine: From Epilepsy & Trigeminal Neuralgia to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Carbamazepine (CBZ) is a well-established antiepileptic and analgesic agent, clinically used for partial seizures, generalized tonic-clonic seizures, and trigeminal neuralgia through voltage-gated sodium channel blockade.
The TxGNN model predicts it may be effective for **Trigeminal Nerve Neoplasm** with a score of **99.998%**, supported by **1 clinical trial** (not yet recruiting; disease entity mismatch) and **20 publications** retrieved for evaluation.
**Critical semantic caution**: The majority of retrieved evidence pertains to trigeminal **neuralgia**, not trigeminal nerve **neoplasm** — these are distinct disease entities, and the TxGNN prediction likely reflects knowledge-graph label proximity rather than a genuine antitumor signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No US FDA license records retrieved (data gap); CBZ is clinically established for epilepsy and trigeminal neuralgia |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| US Market Status | No records found (data gap — manual FDA Orange Book verification recommended) |
| Number of NDAs | 0 (data gap) |
| Recommended Decision | Research Question |

---

## Why Is This Prediction Reasonable?

Carbamazepine is the gold-standard first-line treatment for trigeminal neuralgia and a widely prescribed antiepileptic. Its primary mechanism is voltage-gated sodium channel blockade in a use-dependent manner — suppressing repetitive, high-frequency neuronal firing at the site of ectopic discharge. Preclinical evidence (PMID 3181365) directly demonstrates that intravenous CBZ inhibits spontaneous ectopic discharges from experimental neuromas in both A-alpha/beta and A-delta fibers at clinically relevant serum concentrations.

Trigeminal nerve neoplasms — including schwannomas, meningiomas, sarcoid granulomas, and malignant lymphomas — can compress or infiltrate the trigeminal nerve, producing secondary neuralgia-like pain that is mechanistically similar to classical trigeminal neuralgia. In this narrow context, CBZ may provide **symptomatic pain relief** by suppressing ectopic discharges triggered by tumor compression. Several case reports in the evidence base (PMID 30741017, PMID 25142539) describe patients presenting with facial pain initially managed with CBZ who were later found to harbor trigeminal nerve lymphoma — confirming that CBZ addresses the pain symptom rather than the underlying tumor.

**However, CBZ has no known antitumor mechanism.** The TxGNN high prediction score is most plausibly driven by disease-label semantic overlap between "trigeminal nerve neoplasm" and "trigeminal neuralgia" within the knowledge graph's disease node structure, rather than a genuine repurposing opportunity targeting the neoplasm itself. This prediction should be interpreted as a **symptom-management overlap**, not a novel oncological indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | Not Yet Recruiting | 120 | MRI-based study of brain network dynamics, microstructure, and blood-brain barrier integrity in trigeminal **neuralgia** patients — evaluates neural plasticity mechanisms. **Disease entity mismatch**: this trial studies neuralgia, not neoplasm; no treatment intervention data applicable |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clinica Croatica | Comprehensive treatment options for trigeminal neuralgia; acknowledges tumor compression as a secondary cause; CBZ confirmed as first-line pharmacotherapy |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | TN among the most painful human conditions; etiology involves vascular compression causing demyelination and aberrant discharge; CBZ is established first-line; surgical options reviewed |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case Report | British Journal of Neurosurgery | Primary neurolymphomatosis of the trigeminal nerve presenting as facial pain; CBZ prescribed without symptom improvement; MRI revealed nerve swelling and mass in Meckel's cave — **directly demonstrates CBZ's failure against the underlying neoplasm** |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Case Report | Rinsho Shinkeigaku | Malignant lymphoma with perineural spread along trigeminal nerve initially presenting as classical TN; improved briefly with CBZ, then became refractory as additional cranial nerve symptoms emerged — confirms CBZ manages pain symptom only |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Animal Study | Experimental Neurology | IV CBZ produced immediate inhibition of spontaneous ectopic discharges from saphenous neuromas at doses of 2.51–11.2 mg/kg; serum levels matched therapeutic range — **core mechanistic rationale for symptom suppression** |
| [9109911](https://pubmed.ncbi.nlm.nih.gov/9109911/) | 1997 | Case Report | Neurology | Post-irradiation neuromyotonia in bilateral facial and trigeminal nerve distribution responded to CBZ — radiation-induced nerve injury model, not neoplasm |
| [12590697](https://pubmed.ncbi.nlm.nih.gov/12590697/) | 2003 | Case Report | Neurosurgery | Isolated trigeminal nerve sarcoid granuloma mimicking trigeminal schwannoma on imaging; differential diagnosis and radiological features compared |
| [32454201](https://pubmed.ncbi.nlm.nih.gov/32454201/) | 2020 | Case Report | World Neurosurgery | Trigeminal schwannoma of pterygopalatine fossa (0.1–0.4% of intracranial tumors); resected via endoscopic endonasal approach — surgical management, no CBZ data |
| [33989821](https://pubmed.ncbi.nlm.nih.gov/33989821/) | 2021 | Case Report | World Neurosurgery | Petroclival meningioma causing TN in <5% of cases; encased fifth nerve resected via Kawase approach — surgical management, no CBZ data |
| [26768887](https://pubmed.ncbi.nlm.nih.gov/26768887/) | 2016 | Case Report | Turkish Neurosurgery | Pituitary adenoma with cavernous sinus invasion presenting as isolated trigeminal neuralgia; extremely rare entity requiring surgical decompression |

---

## US Market Information

No US FDA license records were retrieved for Carbamazepine in this Evidence Pack. This represents a **data gap** in the automated query pipeline. Carbamazepine (marketed as Tegretol®, Carbatrol®, Epitol®, Equetro®, and Carnexiv® IV formulation) is in fact an established marketed drug in the United States with approved indications for epilepsy and trigeminal neuralgia. Manual verification via the FDA Orange Book is strongly recommended before regulatory assessment.

---

## Safety Considerations

No TFDA or US FDA warning/contraindication data was retrieved in this Evidence Pack. Please refer to the package insert for complete safety information.

**Clinically established safety signals for Carbamazepine** (requiring formal verification from package insert):

- **Aplastic anemia and agranulocytosis**: Black Box warning; rare but potentially fatal; baseline CBC with differential required before initiation
- **Serious dermatologic reactions**: Stevens-Johnson syndrome (SJS) and toxic epidermal necrolysis (TEN); significantly elevated risk in patients carrying the HLA-B\*1502 allele (prevalence in East and Southeast Asian populations)
- **Teratogenicity**: Associated with spina bifida and neural tube defects; Category D in pregnancy
- **Hyponatremia/SIADH**: Clinically significant, especially in elderly patients
- **Drug interactions**: Potent CYP3A4 inducer with extensive DDI profile; no formal DDI data retrieved in this pack

---

## Conclusion and Next Steps

**Decision: Research Question (Hold)**

**Rationale:**
The TxGNN prediction score of 99.998% for trigeminal nerve neoplasm most likely reflects disease-label semantic proximity within the knowledge graph — the "trigeminal" node connects neuralgia and neoplasm — rather than a genuine antitumor repurposing opportunity. CBZ's symptom-management role in neoplasm-induced neuropathic pain is already within the drug's established standard-of-care use (treating secondary trigeminal neuralgia), and does not constitute a novel repurposing indication. Evidence level L4 (one animal study as the core mechanistic paper; case reports confirming CBZ addresses symptoms, not the tumor) is insufficient to advance to clinical development for the neoplasm itself.

**To proceed, the following is needed:**

- **Clarify the research question**: Is the target "CBZ for pain management secondary to trigeminal nerve neoplasm" (symptom relief — already within standard of care) or "CBZ as an antineoplastic agent" (no established biological basis)?
- **Retrieve US FDA regulatory data**: Confirm CBZ's approved US indications, Black Box warnings, and complete contraindication list from the FDA Orange Book and full prescribing information
- **Confirm MOA data from DrugBank**: Formally document sodium channel blocking mechanism and any secondary pharmacological targets
- **Knowledge graph audit**: Investigate whether the TxGNN training data conflates "trigeminal neuralgia" and "trigeminal nerve neoplasm" disease nodes — if confirmed, the high score reflects a label artifact rather than a biological prediction
- **Disease-specific literature search**: If the intent is symptomatic management in neoplasm patients specifically, a focused PubMed search on "carbamazepine + trigeminal nerve tumor/neoplasm/schwannoma + pain management" with a systematic review methodology would be more informative than the current broad query
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

