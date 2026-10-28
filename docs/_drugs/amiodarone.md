---
layout: default
title: Amiodarone
parent: Moderate Evidence (L3-L4)
nav_order: 328
evidence_level: L4
indication_count: 10
monitor_inn: "AMIODARONE"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
last_modified_at: 2026-10-28
description: "Amiodarone: predicted new indication Catecholaminergic polymorphic ventricular tachycardia (evidence level L5). Approved use: Ventricular fibrillation"
---

# Amiodarone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Amiodarone: From Ventricular Fibrillation to Catecholaminergic Polymorphic Ventricular Tachycardia
{: .text-alpha }

## One-Sentence Summary

Amiodarone is a multi-channel antiarrhythmic originally used to treat ventricular fibrillation.
The TxGNN model predicts it may be effective for **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, but this top-ranked prediction has **0 clinical trials** and only **9 publications** (cohort descriptions, case reports and reviews), with no controlled evidence of benefit.
Among the ten predictions, the best-supported is **ventricular tachycardia** (a closely related arrhythmia), backed by **18 registered trials** (including several Phase 3 and 4 trials) and **20 publications**. It is discussed in the sections below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular fibrillation (the US license records contain no indication text) |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia (rank 1); the best-supported alternative is ventricular tachycardia (rank 3) |
| TxGNN Prediction Score | 0.9978 (CPVT); 0.9964 (ventricular tachycardia) |
| Evidence Level | L4 (CPVT); L1 (ventricular tachycardia) |
| US Market Status | Marketed (valid licenses on record: at least 12) |
| Number of NDAs | 12 (1 NDA and 11 ANDAs) |
| Recommended Decision | Hold (CPVT); Proceed with Guardrails (ventricular tachycardia) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, amiodarone is a class III antiarrhythmic that also has sodium-channel, calcium-channel and beta-adrenergic blocking properties. In theory this broad activity could suppress catecholamine-triggered ventricular arrhythmias.

For **CPVT**, the link is weak. CPVT is driven by calcium-handling defects (RYR2/CASQ2). Standard care is beta-blockers, flecainide and sympathetic denervation. In the retrieved literature, amiodarone appears mainly as a rescue option in refractory arrhythmias, with no controlled evidence of benefit.

For **ventricular tachycardia**, the link is much stronger. Prolonging the action potential and refractoriness is directly relevant to re-entrant ventricular tachycardia. This is largely an extension within the same disease family as the original indication (ventricular fibrillation) rather than true repurposing.

The remaining predictions are not supported:
- **Incessant infant ventricular tachycardia:** There is a randomized trial and an infant study, but they mainly cover supraventricular tachyarrhythmias, so applicability is limited.
- **Rheumatoid arthritis, gout and the other lower-ranked predictions:** These have no plausible therapeutic mechanism. The literature for rheumatoid arthritis and gout concerns adverse effects and drug interactions, so the high scores likely reflect similarities the TxGNN model (deep learning) learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

No clinical trials are registered for CPVT (the rank-1 prediction). The table below shows the most relevant trials for **ventricular tachycardia** (rank 3), which is the best-supported prediction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000531](https://clinicaltrials.gov/study/NCT00000531) | Phase 3 | Completed | N/A | AVID: implantable defibrillator vs. antiarrhythmic drugs (mainly amiodarone) in survivors of life-threatening ventricular arrhythmias |
| [NCT01401647](https://clinicaltrials.gov/study/NCT01401647) | Phase 3 | Completed | 3024 | Amiodarone, lidocaine or placebo in out-of-hospital cardiac arrest due to VF/pulseless VT |
| [NCT00383799](https://clinicaltrials.gov/study/NCT00383799) | Phase 4 | Terminated | 302 | PROCAMIO: IV amiodarone vs. procainamide in well-tolerated wide-QRS tachycardia |
| [NCT03299517](https://clinicaltrials.gov/study/NCT03299517) | Phase 4 | Unknown | 80 | Amiodarone vs. lidocaine in stable VT in the emergency room |
| [NCT00257959](https://clinicaltrials.gov/study/NCT00257959) | Phase 4 | Completed | 400 | OPTIC: amiodarone plus beta-blocker vs. beta-blocker alone vs. sotalol for preventing ICD shocks |
| [NCT02830360](https://clinicaltrials.gov/study/NCT02830360) | Phase 4 | Completed | 416 | VANISH2: catheter ablation vs. antiarrhythmic drug therapy after myocardial infarction |
| [NCT01722942](https://clinicaltrials.gov/study/NCT01722942) | N/A | Unknown | 1100 | CHAGASICS: amiodarone vs. ICD for primary prevention in Chagas cardiomyopathy |
| [NCT01097330](https://clinicaltrials.gov/study/NCT01097330) | Phase 3 | Terminated | 12 | Catheter ablation vs. amiodarone for shock prevention in ICD patients |
| [NCT03855826](https://clinicaltrials.gov/study/NCT03855826) | Phase 4 | Unknown | 756 | Nifekalant vs. amiodarone in VT/VF (amiodarone is a comparator, so relevance is indirect) |
| [NCT03734562](https://clinicaltrials.gov/study/NCT03734562) | N/A | Completed | 180 | Substrate ablation vs. antiarrhythmic drugs for scar-related monomorphic VT |

---

## Literature Evidence

Literature for **ventricular tachycardia** (rank 3), listed as RCT first, then reviews and cohorts. For CPVT, the retrieved literature is limited to cohort studies, a systematic review, a general review and case reports (for example PMID 35892906, 26513538).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27354046](https://pubmed.ncbi.nlm.nih.gov/27354046/) | 2017 | RCT | European Heart Journal | PROCAMIO: randomized comparison of IV procainamide vs. amiodarone for tolerated wide-QRS tachycardia |
| [41217320](https://pubmed.ncbi.nlm.nih.gov/41217320/) | 2026 | Randomized trial substudy | J Am Coll Cardiol | VANISH2 substudy: catheter ablation vs. sotalol or amiodarone for VT |
| [20730062](https://pubmed.ncbi.nlm.nih.gov/20730062/) | 2010 | Review | Vasc Health Risk Manag | Amiodarone as a leading therapy for termination and prevention of VF/VT |
| [9137212](https://pubmed.ncbi.nlm.nih.gov/9137212/) | 1997 | Review | J Am Coll Cardiol | IV amiodarone for malignant and resistant ventricular arrhythmias |
| [28900864](https://pubmed.ncbi.nlm.nih.gov/28900864/) | 2017 | Review | Curr Cardiol Rep | When to medicate and when to ablate in VT with ICD shocks |
| [36878200](https://pubmed.ncbi.nlm.nih.gov/36878200/) | 2023 | Review | Cardiology | Pharmacotherapy in ventricular arrhythmias |
| [30084131](https://pubmed.ncbi.nlm.nih.gov/30084131/) | 2018 | Cohort | Emerg Med Australas | Safety and efficacy of paramedic-administered amiodarone for stable VT |
| [37380314](https://pubmed.ncbi.nlm.nih.gov/37380314/) | 2023 | Trial analysis | JACC Clin Electrophysiol | VT and ICD therapy burden with ablation vs. escalated antiarrhythmic drugs |
| [10666663](https://pubmed.ncbi.nlm.nih.gov/10666663/) | 2000 | Review | Curr Opin Cardiol | Amiodarone primary and secondary prevention trials (EMIAT, CAMIAT) |
| [8258259](https://pubmed.ncbi.nlm.nih.gov/8258259/) | 1993 | Case report | Clin Pharm | Amiodarone-induced thyroid dysfunction |

---

## US Market Information

The drug is marketed in the US, with 12 valid licenses. The records contain no approved-indication text. Five representative authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022325 | Nexterone (Baxter Healthcare) | Injection, solution | Not recorded (valid) |
| ANDA204550 | Amiodarone Hydrochloride (AuroMedics) | Injection, solution | Not recorded (valid) |
| ANDA218253 | Amiodarone Hydrochloride (Zhejiang Poly Pharm.) | Injection, solution | Not recorded (valid) |
| ANDA079029 | Amiodarone Hydrochloride (Zydus) | Tablet | Not recorded (valid) |
| ANDA075389 | Amiodarone Hydrochloride (Dr. Reddy's) | Tablet | Not recorded (valid) |

Available forms are oral tablets and injectable solutions.

---

## Safety Considerations

Package-insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for these.

- **Contraindication-related conditions (not label text):** long QT syndrome (including familial), torsades de pointes, atrioventricular block, sick sinus syndrome, hypothyroidism and hyperthyroidism (including Graves disease and thyrotoxicosis), liver disease and drug-induced liver injury, interstitial lung disease, eosinophilic pneumonia, hypersensitivity pneumonitis, optic neuritis and optic nerve disease, peripheral neuropathy, potassium deficiency, gallbladder disease and corneal deposits.
- **Drug interactions:** 100 interactions were identified. Major-level examples from the first 20 listed include amphotericin B (and its lipid formulations), cisapride, clarithromycin, clotrimazole, dexamethasone, hydrocortisone, dolasetron, eliglustat and agalsidase beta. Moderate-level examples include famotidine, cimetidine, aprepitant, bisacodyl and budesonide.
- **Literature signals:** Thyroid dysfunction, pulmonary toxicity (including fibrosis and diffuse alveolar hemorrhage), and rhabdomyolysis when combined with statins and azoles are reported in the retrieved publications. Pediatric use also raises concerns about thyroid effects, hypotension and proarrhythmia.

---

## Conclusion and Next Steps

**Decision: Hold (CPVT, the top-ranked prediction); Proceed with Guardrails (ventricular tachycardia, the best-supported prediction)**

**Rationale:**
- For CPVT, there are no registered trials and no controlled evidence, and standard care (beta-blockers, flecainide, sympathetic denervation) is well established, so this should be held.
- Ventricular tachycardia is supported by completed Phase 3 trials and multiple Phase 4 comparative trials (L1), but it is essentially an extension of the original indication.
- The remaining predictions (obsolete bundle branch block, rheumatoid arthritis, brachydactyly-syndactyly syndrome, heparin cofactor 2 deficiency, trichotillomania, colobomatous microphthalmia-rhizomelic dysplasia syndrome and gout) lack supporting evidence or a plausible mechanism and should be held. Incessant infant VT is a research question only.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications from the FDA label, which block formal safety screening
- Detailed mechanism of action data
- Verification of the US regulatory status, since the drug is marketed with 12 valid licenses
- A monitoring plan covering thyroid, pulmonary, hepatic and ocular toxicity, QT prolongation and drug interactions
- For CPVT, a mechanistic justification and controlled data versus beta-blockers and flecainide before reconsidering
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

