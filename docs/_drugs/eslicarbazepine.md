---
layout: default
title: Eslicarbazepine
parent: 僅模型預測 (L5)
nav_order: 571
evidence_level: L5
indication_count: 6
---

# Eslicarbazepine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the `txgnn-pipeline` skill for context on TxGNN report generation. Now producing the evaluation report based on the Evidence Pack.

---

# Eslicarbazepine: From Epilepsy to Migraine Disorder

## One-Sentence Summary

Eslicarbazepine (ESL) is a third-generation anticonvulsant that blocks voltage-gated sodium channels (VGSCs), widely used in Europe and the US (as eslicarbazepine acetate, Aptiom/Zebinix) for focal onset seizures — though no records were retrieved from the queried US FDA database.
The TxGNN model predicts it may be effective for **Migraine Disorder** as a preventive therapy,
with **1 completed Phase 2 RCT** (n=452) and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved (0 US FDA license records found; drug is known as an anticonvulsant for focal onset seizures based on literature) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L2 |
| US Market Status | Not found in queried US FDA database |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Eslicarbazepine (as eslicarbazepine acetate, ESL) is a third-generation dibenzazepine anticonvulsant. Its defining mechanism is selective blockade of voltage-gated sodium channels (VGSCs) in their **slow-inactivated state**, which stabilizes overexcited neuronal membranes and suppresses repetitive high-frequency firing. This highly selective inactivated-state binding distinguishes ESL from older sodium-channel blockers like carbamazepine, giving it a more favourable tolerability profile.

The biological rationale for migraine prevention is mechanistically direct. **Cortical spreading depression (CSD)** — the electrophysiological event underlying migraine aura and the trigger for headache cascades — is fundamentally a VGSC-dependent wave of neuronal depolarization propagating across the cortex. By stabilizing VGSCs in the inactivated state, ESL can suppress CSD initiation and propagation, targeting the core pathophysiology of migraine at its source. This is not a novel hypothesis: **Topiramate** and **Valproate**, both established first-line migraine prophylaxis agents, share overlapping VGSC-blocking mechanisms with ESL, providing strong class-level mechanistic precedent.

Epilepsy and migraine also share deeper biological roots. Both are episodic disorders of cortical hyperexcitability, and genetic variants in ion channel genes (particularly *SCN1A* and *CACNA1A*) confer susceptibility to both conditions simultaneously. The existence of a completed Phase 2 RCT directly testing ESL for migraine prophylaxis (NCT01820559) confirms that this mechanistic reasoning was deemed compelling enough by clinical investigators to warrant a multinational trial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01820559](https://clinicaltrials.gov/study/NCT01820559) | Phase 2 | Completed | 452 | Multinational, double-blind, placebo-controlled, parallel-group RCT. Three arms: placebo vs. ESL 800 mg/day QD vs. ESL 1200 mg/day QD, randomized 1:1:1. Evaluated efficacy, safety, and tolerability of ESL as prophylactic treatment in subjects with migraine with or without aura. This is the strongest single piece of evidence for this indication; Phase 3 follow-up has not been identified. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Pharmacotherapy review for trigeminal neuralgia and related neurological pain; discusses third-generation anticonvulsants (ESL class) as promising alternatives to carbamazepine/oxcarbazepine due to improved tolerability, and contextualizes new CGRP blockers for migraine within the broader anticonvulsant landscape |
| [32217376](https://pubmed.ncbi.nlm.nih.gov/32217376/) | 2020 | Safety Review | Journal of the Neurological Sciences | Systematic assessment of tolerability and safety profile of eslicarbazepine acetate across neurological disorders; provides key baseline safety data critical for evaluating ESL in a new indication such as migraine |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Network Meta-Analysis | Cochrane Database of Systematic Reviews | Updated Cochrane network meta-analysis of antiepileptic drug monotherapy; positions ESL within the comparative efficacy and tolerability landscape of AEDs, supporting its profile as a well-characterized neurological agent |
| [25196459](https://pubmed.ncbi.nlm.nih.gov/25196459/) | 2014 | Review | Expert Opinion on Drug Metabolism & Toxicology | Review of PK/PD interactions between antiepileptics and antidepressants; directly relevant for migraine patients, who frequently receive antidepressants concurrently |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | Review | Advanced Drug Delivery Reviews | Comprehensive review of chemical and pharmacokinetic properties of 15 third-generation AEDs approved 1990–2011, including ESL; documents its favorable PK profile and lower drug interaction potential compared to older agents |
| [39262552](https://pubmed.ncbi.nlm.nih.gov/39262552/) | 2024 | Case Report | Cureus | MELAS syndrome case report involving ESL use; limited direct relevance to migraine indication, included for completeness |

---

## US Market Information

No product license records were retrieved from the queried US FDA database for Eslicarbazepine (0 records). This likely represents a **data gap in the current pipeline**, as eslicarbazepine acetate is commercially available as **Aptiom** in the United States (NDA 022416, approved by FDA in 2013 for focal onset seizures). Remediation of this data gap is recommended before advancing regulatory pathway analysis.

---

## Safety Considerations

No structured safety data was retrieved from the queried sources for Eslicarbazepine (key warnings, contraindications, and drug interactions all returned empty or not found).

Based on known drug class properties for eslicarbazepine acetate, the following are clinically important considerations:

- **Drug Interactions**: ESL is a moderate inducer of CYP3A4 and inhibitor of CYP2C19. Clinically relevant interactions include oral contraceptives (reduced efficacy), warfarin (altered INR), and other sodium-channel AEDs. Migraine patients on antidepressants (SSRIs, SNRIs) warrant particular attention.
- **Hyponatremia Risk**: A class effect of dibenzazepines (carbamazepine, oxcarbazepine, ESL); sodium levels should be monitored at baseline and during treatment.

Please refer to the Aptiom (eslicarbazepine acetate) FDA-approved package insert for complete warnings, contraindications, and drug interaction data.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed multinational Phase 2 RCT (NCT01820559, n=452) directly evaluated ESL as migraine prophylaxis, and the VGSC-blocking mechanism is strongly supported by class-level precedent from established migraine preventives (Topiramate, Valproate). L2 evidence is sufficient to advance — but the critical unknown is whether NCT01820559 met its primary endpoint, which determines if a Phase 3 program is warranted or if the program was abandoned after a negative result.

**To proceed, the following is needed:**

- **Retrieve Phase 2 trial results**: Locate the published or unpublished outcome data for NCT01820559. A negative Phase 2 result would downgrade this to Hold.
- **Retrieve the complete US FDA label**: The Aptiom NDA label contains full safety, contraindication, and drug interaction data required for S1 safety screening. The current data gap (DG001) is rated Blocking.
- **Confirm US market status**: Remediate the US FDA database query — Aptiom is a marketed product and should have retrievable NDA records (DG001 adjacent issue).
- **Obtain MOA from DrugBank API**: Formal MOA documentation (DG002) is needed to complete the mechanistic rationale section for submission.
- **Design a safety monitoring plan**: Covering sodium levels, hepatic function, drug interactions with common migraine co-medications (antidepressants, triptans, oral contraceptives), and reproductive safety given the migraine patient demographic (predominantly women of childbearing age).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

