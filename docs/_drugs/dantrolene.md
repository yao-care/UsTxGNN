---
layout: default
title: Dantrolene
parent: 僅模型預測 (L5)
nav_order: 568
evidence_level: L5
indication_count: 9
---

# Dantrolene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Dantrolene: From Skeletal Muscle Relaxation to Malignant Hyperthermia Susceptibility

## One-Sentence Summary

Dantrolene sodium is a direct-acting skeletal muscle relaxant and the only specific pharmacological treatment for malignant hyperthermia (MH) currently recognized in international clinical practice.
The TxGNN model predicts it may be effective for **malignant hyperthermia, susceptibility to** — a prediction that aligns precisely with dantrolene's established global clinical use targeting the RyR1 calcium release channel.
Supporting evidence includes **0 registered clinical trials** (ethically infeasible for this acute lethal emergency) and **19 publications** comprising consensus guidelines from major anesthesia societies and multiple systematic reviews.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication in Taiwan (drug not currently marketed) |
| Predicted New Indication | Malignant Hyperthermia, Susceptibility To |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 (international consensus guidelines and systematic reviews; Phase 3 RCTs are ethically infeasible for an acute life-threatening emergency with an established antidote) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Taiwan Approvals | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dantrolene exerts its pharmacological effect by directly inhibiting the skeletal muscle ryanodine receptor type 1 (RyR1) — the sarcoplasmic reticulum calcium release channel central to excitation-contraction coupling. In a malignant hyperthermia (MH) crisis, triggering agents such as volatile anesthetics (halothane, sevoflurane, desflurane) or succinylcholine cause uncontrolled, runaway Ca²⁺ release through mutant RyR1 channels, leading to explosive muscle hypermetabolism, hyperthermia, acidosis, and rhabdomyolysis. Dantrolene arrests this cascade at its molecular origin by blocking the very channel responsible — making it a mechanistically precise, cause-targeted intervention rather than symptomatic management.

Malignant hyperthermia susceptibility (MHS) arises almost exclusively from autosomal dominant gain-of-function mutations in *RYR1* (rarely *CACNA1S*), which pathologically sensitize the calcium release channel to anesthetic triggers. The direct molecular overlap between dantrolene's target (RyR1) and the MH disease-causing gene (RYR1) represents one of the clearest pharmacogenomic target-disease linkages in clinical medicine. The TxGNN model's top score of 99.93% reflects this exceptionally tight mechanistic alignment. Notably, TxGNN also ranked several related RyR1-spectrum disorders in the top 9 predictions — including King-Denborough syndrome (rank 3), central core disease (rank 5), and centronuclear myopathy (rank 9) — which further validates the biological coherence of the RyR1 network signal.

It is critical to recognize that dantrolene's role in MH is not a novel repurposing hypothesis: it has been the internationally recognized specific treatment for acute MH since the early 1980s, endorsed by the Association of Anaesthetists (2021) and the European Malignant Hyperthermia Group (2021). What the TxGNN prediction actually surfaces is a regulatory and patient-safety gap — dantrolene is absent from Taiwan's TFDA registry, meaning it is unavailable as an emergency stocking agent in Taiwanese anesthesia departments.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in ClinicalTrials.gov or ICTRP for dantrolene in malignant hyperthermia susceptibility.

> **Why no trials exist**: MH is a rare (incidence 1:10,000–1:250,000 anesthetics), acute, potentially lethal emergency. Once MH is recognized and triggered, withholding dantrolene to serve a placebo arm is ethically untenable. Evidence has therefore accumulated through case series, pharmacological studies, and expert consensus rather than formal RCTs. This is analogous to other acute emergency treatments (e.g., epinephrine for anaphylaxis) where RCT methodology is not applicable.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Clinical Guideline | Anaesthesia | Association of Anaesthetists 2020 MH guideline: defines dantrolene as the specific treatment; provides dosing and monitoring protocol for acute MH crisis |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Consensus Guideline | British Journal of Anaesthesia | European Malignant Hyperthermia Group consensus on perioperative management of confirmed or suspected MH-susceptible patients |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Review | Critical Care Medicine | Expert narrative review of MH clinical epidemiology and ICU management; dantrolene as cornerstone of crisis therapy |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Review | Orphanet Journal of Rare Diseases | Comprehensive review covering MH pharmacogenetics, incidence (1:10,000–1:250,000), triggering agents, and dantrolene efficacy |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Review | Anesthesiology Clinics | MH update: RyR1 Ca²⁺ channel pathology, autosomal dominant inheritance, improved survival correlated with dantrolene availability |
| [40597248](https://pubmed.ncbi.nlm.nih.gov/40597248/) | 2025 | Bibliometric Analysis | Orphanet Journal of Rare Diseases | Global bibliometric analysis 1975–2024: research trends show mortality reduction driven by dantrolene adoption and guideline dissemination |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mechanistic Study | PNAS | Demonstrates that dantrolene requires Mg²⁺ to arrest MH; elucidates the precise biophysical mechanism of RyR1 channel inhibition |
| [17456235](https://pubmed.ncbi.nlm.nih.gov/17456235/) | 2007 | Review | Orphanet Journal of Rare Diseases | Incidence, genetics, and management of MH; dantrolene pharmacology and emergency protocol |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Review | Postgraduate Medical Journal | Autosomal dominant MH susceptibility; identifies dantrolene sodium as the definitive treatment for acute crisis |
| [33863282](https://pubmed.ncbi.nlm.nih.gov/33863282/) | 2021 | Clinical Observation | BMC Anesthesiology | Clinical outcomes of MH in settings where dantrolene is not readily available (e.g., China); highlights mortality consequences of dantrolene absence |

---

## Taiwan Market Information

Dantrolene (DrugBank: DB01219) currently has **no approved products** registered with Taiwan's TFDA. No authorization numbers, dosage forms, or approved indications are on record. The drug is not marketed and is not available through standard supply channels in Taiwan.

> **Global reference context**: Internationally, dantrolene sodium is approved in the United States across multiple NDAs — including Dantrium® (capsules and IV), Revonto® (IV), and Ryanodex® (IV suspension) — for the treatment and prevention of malignant hyperthermia and for chronic management of skeletal muscle spasticity. Ryanodex® offers a faster reconstitution profile that is particularly relevant for the acute emergency setting.

---

## Safety Considerations

TFDA package insert data was not available at the time of this report. Based on the established global safety profile of dantrolene:

- **Hepatotoxicity**: The most clinically significant concern with oral (chronic) use — symptomatic hepatitis has been reported, with fatalities documented at higher doses. Liver function monitoring is required for oral administration.
- **Muscle Weakness**: Expected pharmacodynamic effect from RyR1 inhibition; may impair respiratory muscle function.
- **Cardiovascular Effects (IV)**: IV dantrolene has been associated with cardiovascular depression in rare cases; monitoring is required in the acute crisis setting.
- **Drug Interactions**: Concurrent use with calcium channel blockers (e.g., verapamil) during MH crisis has been associated with cardiovascular collapse; use with caution.

> Please refer to the prescribing information (Dantrium/Revonto/Ryanodex package inserts) for the complete safety profile. Formal TFDA warning and contraindication text should be obtained from the original package insert filing before any regulatory submission.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dantrolene is the sole internationally recognized specific pharmacological treatment for malignant hyperthermia, supported by consensus guidelines from the Association of Anaesthetists (2021) and the European Malignant Hyperthermia Group (2021). Its complete absence from Taiwan's drug registry represents a patient safety risk: any Taiwanese medical facility administering volatile anesthetics or succinylcholine currently lacks access to the only drug capable of reversing a potentially fatal MH crisis. TxGNN's 99.93% prediction score reflects the perfect mechanistic alignment between dantrolene's RyR1-inhibiting mechanism and the RYR1 mutation-driven pathophysiology of MH susceptibility.

**To proceed, the following is needed:**

- **Regulatory filing**: Submit TFDA NDA application with the existing global safety and efficacy data package (US FDA approvals serve as the primary reference)
- **MOA documentation**: Formally complete the mechanism-of-action assessment (DG002) using DrugBank API or published pharmacological literature on RyR1 inhibition
- **TFDA warning data**: Obtain and parse TFDA package insert equivalent (DG001) to complete the Taiwan-specific safety profile
- **Emergency formulary protocol**: Develop hospital-level formulary listing and mandatory stocking guidelines for all anesthesia departments and operating rooms across Taiwan
- **Supply chain planning**: Establish cold-chain logistics for IV dantrolene (particularly Ryanodex®, which offers faster reconstitution for acute emergencies)
- **Education**: Disseminate MH recognition and dantrolene administration training in alignment with Taiwan's anesthesia societies
- **Pharmacovigilance plan**: Implement hepatotoxicity monitoring protocol for any off-label oral use in chronic spasticity conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

