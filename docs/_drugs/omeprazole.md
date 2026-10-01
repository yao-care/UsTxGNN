---
layout: default
title: Omeprazole
parent: Moderate Evidence (L3-L4)
nav_order: 993
evidence_level: L3
indication_count: 2
---

# Omeprazole
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **2** 
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

# Omeprazole: From Acid-Related Gastric Disorders to Duodenogastric Reflux

## One-Sentence Summary

Omeprazole is a proton pump inhibitor (PPI) that suppresses gastric acid. The Evidence Pack does not list its label indications, so its original use is described here from its drug class.
The TxGNN model predicts it may be useful for **duodenogastric reflux**, but only **1 clinical trial** (a diagnostic imaging study that does not test omeprazole) and **20 publications** (mostly small physiological or animal studies) are linked to this prediction.
Two animal studies also raise a safety question: acid blockade combined with duodenogastric reflux may promote gastric cancer in rats.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided (all retrieved US licenses have empty indication text) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the record. Omeprazole belongs to the proton pump inhibitor class, which lowers gastric acidity.

Duodenogastric reflux is the backflow of bile and duodenal contents into the stomach. Omeprazole does not directly address this. It reduces acid, but it does not stop bile or duodenal juice from refluxing. A few small human studies, mostly in Barrett's esophagus, measured omeprazole's effect on duodenogastric and bile reflux. This report cannot judge their results from the titles and abstract fragments alone.

The very high TxGNN score is a computational prediction from the knowledge graph, not clinical evidence. Two rat studies also suggest that acid blockade plus duodenogastric reflux may increase gastric carcinogenesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | NA | Completed | 157 | Endoscopic tri-modal imaging to distinguish functional dyspepsia from reflux disease. It is a diagnostic study and does not test omeprazole, so it gives no efficacy evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Clinical study (human) | Scand J Gastroenterol | Effect of omeprazole on antral duodenogastric reflux in Barrett's esophagus. Notes that recent work suggests omeprazole may reduce duodenogastric reflux. |
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Clinical study (human) | Gut | Effect of omeprazole 20 mg twice daily on duodenogastric and gastro-oesophageal bile reflux in Barrett's esophagus. |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Prospective study (children) | J Pediatr Gastroenterol Nutr | Effect of omeprazole on oesophageal bile reflux in children. |
| [11232672](https://pubmed.ncbi.nlm.nih.gov/11232672/) | 2001 | Clinical study (human) | Am J Gastroenterol | Compares acid and bile reflux in Barrett's esophagus vs. reflux esophagitis and tests PPI therapy. |
| [9841990](https://pubmed.ncbi.nlm.nih.gov/9841990/) | 1998 | Clinical study (human) | J Gastrointest Surg | Bile reflux in benign and malignant Barrett's esophagus after medical acid suppression or Nissen fundoplication. |
| [19491829](https://pubmed.ncbi.nlm.nih.gov/19491829/) | 2009 | Clinical study (human) | Am J Gastroenterol | Compares duodenogastroesophageal and acid reflux between PPI responders and non-responders on once-daily PPI. |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Animal study (rat) | Dig Dis Sci | Acid blockade with omeprazole promoted gastric carcinogenesis induced by duodenogastric reflux. |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Animal study (rat) | Acta Cir Bras | Tests whether omeprazole protects against gastric adenocarcinoma in rats with duodenogastric reflux. |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Animal study (rat) | Dig Dis Sci | Duodenogastric reflux stimulates foregut mucosal growth, potentiated by acid blockade (including omeprazole). |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal study (rat) | Gastric Cancer | Lansoprazole (not omeprazole) promoted gastric carcinogenesis in rats with duodenogastric reflux. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022032 | omeprazole (Publix Super Markets Inc) | Tablet, delayed release | Not provided |
| ANDA212977 | Omeprazole (REMEDYREPACK INC.) | Capsule, delayed release | Not provided |
| ANDA203270 | Omeprazole (Rising Pharma Holdings, Inc.) | Capsule, delayed release | Not provided |
| NDA209400 | omeprazole (H E B) | Tablet, orally disintegrating, delayed release | Not provided |
| ANDA091672 | Omeprazole (Preferred Pharmaceuticals Inc.) | Capsule, delayed release | Not provided |

All listed forms are oral.

---

## Safety Considerations

- **Carcinogenesis signal (animal data):** Two rat studies (PMIDs 10389684, 8943968) found that gastric acid blockade with omeprazole, combined with duodenogastric reflux, promoted mucosal growth and gastric carcinogenesis. The 2020 rat study (PMID 33027361) examined the same question, but its result cannot be judged from the abstract fragment. Relevance to humans is unknown.
- **Package insert data:** Warnings, contraindications and drug interaction data were not retrieved. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only linked clinical trial is unrelated to omeprazole treatment, and the human literature consists of small physiological studies in Barrett's esophagus with unassessed results. Animal data suggest acid suppression could worsen outcomes in duodenogastric reflux, so the very high TxGNN score does not justify advancing.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Full-text review of the human studies (PMIDs 10994616, 9824338, 16641575, 11232672) to see whether omeprazole actually reduces duodenogastric or bile reflux
- An assessment of the gastric carcinogenesis risk in patients with duodenogastric reflux
- Route and dosage form compatibility check (currently pending)

The second predicted indication, duodenal obstruction (score 99.64%), is also on Hold at evidence level L4. No retrieved evidence shows omeprazole treating it, and acid suppression cannot relieve an established mechanical obstruction.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

