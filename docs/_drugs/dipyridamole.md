---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 613
evidence_level: L5
indication_count: 10
---

# Dipyridamole
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

Using the txgnn-pipeline context from the project setup, I'll note one important analytical decision before presenting the report: the evidence pack itself flags TxGNN's #1-ranked prediction (Prinzmetal angina) as a likely false positive driven by *diagnostic* co-occurrence (dipyridamole stress-testing literature) rather than *therapeutic* evidence — one PMID (3421166) even documents dipyridamole *inducing* coronary vasospasm requiring aminophylline rescue. Presenting that as the flagship "new indication" would be clinically misleading. The pack's own strongest, best-supported candidate is **stroke / TIA secondary prevention** (rank 2 and rank 5, both L1 evidence, "Proceed with Guardrails"), which is also mechanistically and clinically coherent with dipyridamole's known antiplatelet pharmacology. I've built the report around that candidate and included a transparent note explaining why the raw top-score prediction was not used as the headline.

---

# Dipyridamole: From Antiplatelet/Coronary Vasodilator Therapy to Ischemic Stroke & TIA Secondary Prevention

## One-Sentence Summary

> Dipyridamole is a phosphodiesterase inhibitor and antiplatelet agent with a long history of use in thromboembolism prophylaxis and, in fixed-dose combination with aspirin (Aggrenox/Asasantin), in cerebrovascular disease.
> The TxGNN model's best-supported prediction is that dipyridamole (combined with aspirin) is effective for **secondary prevention of ischemic stroke and transient ischemic attack (TIA)**,
> a direction already supported by **31 clinical trials** (including two landmark Phase 4 RCTs enrolling >24,000 patients combined) and **18–20 publications**, several of which are Cochrane systematic reviews and meta-analyses.

> ⚠️ **Note on ranking**: TxGNN's numerically highest-scoring prediction for this drug is "Prinzmetal angina" (score 99.99%, rank 381). However, the underlying literature for that candidate consists almost entirely of dipyridamole used as a *pharmacologic stress-test agent* to diagnose or provoke coronary vasospasm — not as a treatment. One cited study (PMID 3421166) explicitly describes dipyridamole *inducing* vasospasm requiring reversal. This is judged to be a **diagnostic co-occurrence artifact, not a genuine treatment signal**, and is carried forward only as a flagged/rejected candidate (see Conclusion). The stroke/TIA candidates below are the credible repurposing signal in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from regulatory records in this evidence pack (0 licenses on file). Based on general pharmacology, dipyridamole is historically used as a coronary vasodilator / antiplatelet agent (e.g., thromboembolism prophylaxis post prosthetic heart valve). |
| Predicted New Indication | Ischemic Stroke (secondary prevention), closely paired with Transient Ischemic Attack |
| TxGNN Prediction Score | 99.95% (stroke disorder, rank 1974) / 99.87% (TIA, rank 4106) |
| Evidence Level | L1 |
| Market Status (per evidence pack) | Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (data gap DG002, High severity). Based on generally known pharmacology, dipyridamole inhibits platelet phosphodiesterase (PDE) and blocks cellular reuptake of adenosine, increasing intracellular cAMP/cGMP and potentiating endogenous adenosine's vasodilatory and antiplatelet-aggregation effects. This is a clinically established mechanism (not merely a model prediction) — the drug is already marketed in fixed-dose combination with aspirin (Aggrenox/Asasantin) specifically for stroke-related indications in multiple jurisdictions.

Dipyridamole's original use profile (antiplatelet / coronary vasodilator, adjunct thromboembolism prophylaxis) and the predicted new indication (ischemic stroke/TIA secondary prevention) sit on the same pharmacological continuum: both rely on inhibiting platelet-mediated thrombus formation in arterial vascular beds. This is not a mechanistic leap — it is largely a *validated* repurposing already reflected in real-world drug combinations (Aggrenox), which explains why the clinical trial evidence for this candidate is unusually mature (large Phase 3/4 RCTs) rather than purely preclinical.

TIA (rank 5, score 99.87%) should be read together with the stroke candidate rather than separately: TIA and ischemic stroke share the same thromboembolic mechanism, and most of the pivotal trials below (ESPRIT, EARLY, JASAP) enrolled mixed TIA/minor-stroke populations. Treating them as one clinical continuum is consistent with how these trials were actually designed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) (ESPRIT) | Phase 4 | Completed | 4,500 | Compared aspirin+dipyridamole vs. aspirin alone for secondary prevention after cerebral ischemia of arterial origin (TIA/minor stroke). Graded "A" — key direct evidence. |
| [NCT00153062](https://clinicaltrials.gov/study/NCT00153062) (PRoFESS) | Phase 4 | Completed | 20,332 | Large RCT: extended-release dipyridamole+aspirin (Aggrenox) vs. clopidogrel for second-stroke prevention. Graded "A" — key direct evidence. |
| [NCT00311402](https://clinicaltrials.gov/study/NCT00311402) (JASAP) | Phase 3 | Completed | 1,295 | Japanese RCT: Aggrenox (ER-dipyridamole 200mg/ASA 25mg BID) vs. aspirin 81mg once daily for prevention of recurrent brain infarction. |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) (EARLY) | Phase 4 | Completed | 551 | Compared early (within 24h) vs. delayed initiation of Aggrenox after acute ischemic stroke/TIA. |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | NA | Completed | 240 | Studied antioxidant activity of dipyridamole (already approved in Italy with aspirin for secondary prevention of cerebral embolism in carotid atherosclerosis) in carotid revascularization patients. |
| [NCT01295567](https://clinicaltrials.gov/study/NCT01295567) | Phase 4 | Completed | 95 | Assessed whether dipyridamole protects against ischemia-reperfusion injury in elective CABG patients. Graded "B" — mechanistically supportive, not a stroke population. |
| [NCT02565693](https://clinicaltrials.gov/study/NCT02565693) | Phase 2 | Completed | 101 | Randomized comparison of apixaban vs. antiplatelet drugs (incl. dipyridamole) after anticoagulation-associated intracerebral haemorrhage in AF patients. Graded "B." |
| [NCT01661322](https://clinicaltrials.gov/study/NCT01661322) | Phase 3 | Terminated | 3,096 | Tested triple antiplatelet therapy (aspirin+clopidogrel+dipyridamole) vs. standard aspirin+dipyridamole in high-risk stroke/TIA patients; terminated early. |
| [NCT00238667](https://clinicaltrials.gov/study/NCT00238667) | Phase 3 | Completed | 250 | Feasibility RCT of anticoagulants vs. antiplatelets (including dipyridamole regimens) in acute cervical artery dissection-related stroke. |
| [NCT01613755](https://clinicaltrials.gov/study/NCT01613755) | Phase 4 | Completed | 18 | Pharmacokinetic interaction study: dipyridamole and metformin, relevant given frequent co-prescription in diabetic stroke/TIA patients. |

*31 trials total were retrieved for this indication; the above 10 were prioritized by direct relevance grading and dipyridamole-specific design.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17636684](https://pubmed.ncbi.nlm.nih.gov/17636684/) | 2007 | Cochrane Systematic Review | Cochrane Database Syst Rev | Adding dipyridamole to aspirin reduced recurrent vascular events by ~22% vs. aspirin alone in patients with cerebral ischemia of arterial origin. |
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Meta-analysis (individual patient data) | Stroke | IPD meta-analysis of RCTs on dipyridamole (± aspirin) for secondary prevention after ischemic stroke/TIA; supports benefit of combination therapy. |
| [11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/) | 2002 | Meta-analysis | BMJ | Antithrombotic Trialists' Collaboration meta-analysis: antiplatelet therapy reduces death/MI/stroke in high-risk patients. |
| [8981292](https://pubmed.ncbi.nlm.nih.gov/8981292/) | 1996 | RCT (ESPS-2) | J Neurol Sci | Pivotal randomized, placebo-controlled, double-blind trial establishing efficacy of ASA + modified-release dipyridamole for secondary stroke prevention. |
| [23871093](https://pubmed.ncbi.nlm.nih.gov/23871093/) | 2013 | Meta-analysis of RCTs | J Neurol Sci | Efficacy/safety of aspirin+dipyridamole vs. aspirin alone after TIA/stroke. |
| [27816341](https://pubmed.ncbi.nlm.nih.gov/27816341/) | 2016 | Review | Presse Med | General review of secondary stroke prevention strategies including antiplatelet regimens. |
| [20955428](https://pubmed.ncbi.nlm.nih.gov/20955428/) | 2010 | Review | Ann NY Acad Sci | Explores dipyridamole's antithrombotic and neuroprotective (non-platelet) benefits in acute stroke. |
| [30649687](https://pubmed.ncbi.nlm.nih.gov/30649687/) | 2019 | Nationwide case-control cohort | CNS Drugs | Dipyridamole+clopidogrel combination for secondary stroke prevention in aspirin-intolerant post-MI patients. |
| [36030623](https://pubmed.ncbi.nlm.nih.gov/36030623/) | 2022 | Cohort | J Neurol Sci | Platelet reactivity after adding dipyridamole to aspirin in early/late phases post-TIA/ischemic stroke. |
| [18342579](https://pubmed.ncbi.nlm.nih.gov/18342579/) | 2008 | Review | Vascular Pharmacology | Reviews dipyridamole's adenosine-transporter/PDE-inhibition mechanism and vascular protective role in cerebrovascular disease. |

*18–20 publications total were retrieved; the above 10 were prioritized (Cochrane reviews/meta-analyses first, then mechanistic and cohort studies).*

---

## Market Information

No license or authorization records were found in this evidence pack (0 total licenses; market status: Not marketed). This appears to be a data completeness gap rather than a definitive absence of marketed products — dipyridamole is known to be marketed elsewhere (e.g., as Persantin and, combined with aspirin, as Aggrenox/Asasantin) — but this evidence pack contains no primary source records to confirm authorization numbers, product names, or approved indication text for the assessed jurisdiction. This should be independently verified before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug–drug interaction (DDI) data were returned for dipyridamole in this evidence pack (DDI query status: not found, 0 interactions). Notably, TFDA package-insert warnings/contraindications are flagged as a **Blocking** data gap (DG001) — this must be resolved before any safety-driven decision (S1 stage) can be made.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The stroke/TIA secondary-prevention candidate is supported by L1-grade evidence — multiple large, completed Phase 3/4 RCTs (ESPRIT n=4,500; PRoFESS n=20,332; JASAP n=1,295) plus five Cochrane-level systematic reviews/meta-analyses — and is mechanistically coherent with dipyridamole's established antiplatelet pharmacology, including real-world precedent via the Aggrenox combination product. This is one of the strongest-evidenced repurposing candidates possible under this framework; however, a **Blocking**-severity safety data gap (missing TFDA labeling) prevents a full "Go" decision.

Separately, the TxGNN model's raw #1-ranked prediction for this drug, Prinzmetal angina, is **not recommended for further investment** — the supporting literature reflects dipyridamole's use as a diagnostic vasospasm-provocation agent, not a therapeutic one, and should be treated as a likely false positive pending manual expert review. Six additional low-ranked candidates (sick sinus syndrome 2, sarcoglycanopathy, Wildervanck syndrome, macrocephaly/dysmorphic facies syndrome, cavernous sinus thrombosis, lateral sinus thrombosis) have L5 evidence with no clinical trials or literature and no plausible mechanistic link (two are standard-of-care anticoagulant-treated conditions where antiplatelet therapy is not first-line) — these are correctly held. "Thrombotic disease" (rank 3, L2) is too broad/heterogeneous a category to act on directly and is better addressed via its more specific components (stroke/TIA) already covered above.

**To proceed, the following is needed:**
- TFDA (or applicable local regulatory) package insert — warnings, contraindications, DDI data (Blocking gap DG001)
- Confirmed mechanism of action from DrugBank API (High-priority gap DG002)
- Verification of actual market/licensing status in the target jurisdiction (evidence pack shows 0 licenses, which conflicts with dipyridamole's known global availability and should be reconciled)
- Route-of-administration compatibility check (currently "pending" in evidence pack)
- Formal expert/pharmacovigilance review to close out the Prinzmetal angina candidate as a rejected false positive, so it does not resurface as an unvetted signal
- A bleeding-risk monitoring plan appropriate to combined antiplatelet therapy (dipyridamole + aspirin), once labeling data is available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

