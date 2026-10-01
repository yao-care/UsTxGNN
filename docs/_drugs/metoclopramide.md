---
layout: default
title: Metoclopramide
parent: Model Prediction Only (L5)
nav_order: 918
evidence_level: L5
indication_count: 5
---

# Metoclopramide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Metoclopramide: Repurposing Prediction for Gastric Ulcer

## One-Sentence Summary

Metoclopramide is a marketed prokinetic and antiemetic (a dopamine D2 antagonist) that acts on gastric motility.
The TxGNN model predicts it may be useful for **gastric ulcer**, but there are only **2 registered clinical trials** (1 loosely related) and **20 publications**, mostly animal studies, reviews and physiology studies.
The evidence is indirect, so this is best treated as a research question rather than a ready candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Gastric ulcer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 (preclinical and mechanistic evidence only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed authorizations are ANDAs, i.e. generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not available in this Evidence Pack. Based on the pack's analysis and the retrieved literature, metoclopramide is a D2 antagonist and 5-HT4 agonist prokinetic. It improves gastric emptying and reduces duodenogastric bile reflux. Its gastrointestinal effects come from antagonizing dopamine's inhibitory action and enhancing acetylcholine release.

The link to gastric ulcer is indirect. Delayed emptying and bile reflux can contribute to gastric mucosal injury, so a prokinetic could plausibly help as an adjunct in ulcer patients with those features. The guinea-pig study suggests protection may come from better gastric drainage and less pyloric reflux, not from lower acid secretion.

The important limit is that metoclopramide has no acid-suppressive or mucosal-healing action, which are the core of standard ulcer therapy. The very high TxGNN score reflects proximity in the knowledge graph, not clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Randomized, double-blind trial of metoclopramide premedication in upper GI bleeding. It asks whether repeat endoscopy, interventional radiology or surgery is needed less often, and whether visualization improves. This is indirect support only, because it does not measure ulcer healing. |
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Completed | 19 | Pharmacist- and data-driven prescribing-safety quality-improvement programme in Scottish primary care. It has no evident link to metoclopramide efficacy in gastric ulcer. |

---

## Literature Evidence

The abstract was unavailable for PMIDs 4779253, 775822 and 19225, so the findings below come from titles only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | RCT (double-blind, n=40) | Yonsei Med J | IV metoclopramide plus ranitidine tested on preoperative gastric contents in laparoscopic gynecologic surgery. Not ulcer-specific. |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | Randomized double-blind crossover (n=12) | MMW Munch Med Wochenschr | In healthy volunteers, metoclopramide and domperidone did not significantly change serum gastrin or gastric acid secretion. |
| [4779253](https://pubmed.ncbi.nlm.nih.gov/4779253/) | 1973 | Clinical physiology study | Curr Med Res Opin | Studied bile reflux in gastric ulcer patients, including the effect of metoclopramide and carbenoxolone. No abstract available. |
| [775822](https://pubmed.ncbi.nlm.nih.gov/775822/) | 1976 | Clinical report (German) | ZFA | Title indicates metoclopramide therapy of gastric and duodenal ulcer. No abstract available. |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal study (rat) | Arch Int Pharmacodyn Ther | Metoclopramide (20 and 50 mg/kg) had an ulcer-protective effect in aspirin-induced and pylorus-ligated ulcer models. |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | Animal study (guinea pig) | Indian J Physiol Pharmacol | Protection against three experimental ulcer types without changing gastric acidity. Likely due to improved gastric drainage and less pyloric reflux. |
| [28652516](https://pubmed.ncbi.nlm.nih.gov/28652516/) | 2017 | Animal study (rat) | J Smooth Muscle Res | Effects of ulcer site and prokinetic drugs on gastric emptying after acetic acid ulceration. |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Ann Intern Med | Pharmacology and clinical use of metoclopramide, including antiemetic and gastrointestinal smooth-muscle stimulatory effects. |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Review | Drugs | Drug treatment of gastric and duodenal ulcer. No abstract available. |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Review | Postgrad Med | Strategies for peptic lesions that resist standard H2-antagonist or sucralfate therapy. |

---

## US Market Information

The pack lists 20 authorizations in total; five are shown below. Approved indication text is not provided in the data. Available forms also include orally disintegrating tablets and injections.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA072801 | Metoclopramide | Tablet | Bryant Ranch Prepack |
| ANDA078807 | Metoclopramide | Tablet | Ipca Laboratories Limited |
| ANDA071402 | Metoclopramide | Solution | Bryant Ranch Prepack |
| ANDA091392 | Metoclopramide | Injection, solution | Fresenius Kabi USA, LLC |
| ANDA070184 | Metoclopramide | Tablet | AvKARE |

---

## Safety Considerations

- **Key Warnings**: Metoclopramide carries a boxed warning for tardive dyskinesia. A published case report also describes neurotoxicity ([PMID 3059051](https://pubmed.ncbi.nlm.nih.gov/3059051/)). Both should be weighed in any repurposing case.

Please refer to the package insert for the full warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Direct ulcer evidence is limited to old animal studies, and the only Phase 4 trial targets endoscopic visualization, not ulcer healing. Metoclopramide does not suppress acid or promote mucosal healing, and its neurological safety signal is significant. The high TxGNN score alone does not justify moving forward. The other predicted indications (gastroduodenitis, peptic ulcer disease, peptic ulcer perforation and gastrojejunal ulcer) are also at Hold, with L4 to L5 evidence.

**To proceed, the following is needed:**
- Approved-indication text and safety data (warnings, contraindications) from the package insert
- Detailed mechanism-of-action data from DrugBank
- Results of NCT05746377, and any trial with ulcer healing or recurrence as the primary endpoint
- A defined target subgroup (for example, ulcer with delayed gastric emptying or bile reflux) and a comparison against standard acid-suppressive therapy
- A risk-benefit assessment covering tardive dyskinesia and treatment duration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

