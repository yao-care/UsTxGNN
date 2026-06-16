---
layout: default
title: Cefprozil
parent: 僅模型預測 (L5)
nav_order: 506
evidence_level: L5
indication_count: 10
---

# Cefprozil
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

Based on the Evidence Pack, here is the full evaluation report:

---

# Cefprozil: From Respiratory and Skin Infections to Urinary Tract Infection

## One-Sentence Summary

Cefprozil is an oral second-generation cephalosporin antibiotic primarily known for treating upper respiratory tract infections (pharyngitis, acute bronchitis, sinusitis) and skin/soft tissue infections, though it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Urinary Tract Infection (UTI)**, with **0 registered clinical trials** and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Upper respiratory tract infections, skin/soft tissue infections (not registered in Taiwan) |
| Predicted New Indication | Urinary Tract Infection |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank record in this Evidence Pack. Based on established pharmacological knowledge, Cefprozil belongs to the second-generation cephalosporin class and works by inhibiting bacterial cell wall synthesis — it binds to penicillin-binding proteins (PBPs) on the bacterial membrane, disrupting peptidoglycan cross-linking and ultimately causing cell lysis. This beta-lactam mechanism is the same one that underpins the entire cephalosporin family's antibacterial efficacy.

What makes the UTI prediction particularly compelling is Cefprozil's coverage of the most common uropathogens. In vitro studies — including a Taiwan-based study — confirm that Cefprozil inhibits over 80% of *Escherichia coli* and *Klebsiella pneumoniae* clinical isolates at achievable concentrations, and it is also active against *Proteus mirabilis*. Together, these three organisms account for the large majority of community-acquired UTIs. Critically, oral Cefprozil achieves high urinary drug concentrations after absorption, which is the key pharmacokinetic requirement for effective UTI treatment.

Three independent randomized comparative trials from the early 1990s directly tested Cefprozil against cefaclor (a reference second-generation cephalosporin with an established UTI indication) and found comparable clinical cure rates of approximately 93–94% in patients with acute uncomplicated UTI. This body of evidence, combined with the mechanistic rationale and favorable oral pharmacokinetics, strongly supports the TxGNN prediction. It is also worth noting that Cefprozil holds FDA approval for UTI treatment in the United States — confirming that this "repurposing" prediction aligns with an internationally recognized clinical use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cefprozil in urinary tract infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1761453](https://pubmed.ncbi.nlm.nih.gov/1761453/) | 1991 | Comparative RCT | J Antimicrobial Chemother | Open-label RCT in 102 adults; Cefprozil 500 mg QD vs. cefaclor 250 mg TID × 10 days for acute uncomplicated UTI — clinical efficacy comparable between groups |
| [1952874](https://pubmed.ncbi.nlm.nih.gov/1952874/) | 1991 | Comparative RCT | Antimicrob Agents Chemother | 108 college women with acute UTI; Cefprozil QD vs. cefaclor TID × 10 days; clinical cure 94% vs. 94%, bacterial cure 93% vs. 94% — not significantly different |
| [1611652](https://pubmed.ncbi.nlm.nih.gov/1611652/) | 1992 | Comparative RCT | Clinical Therapeutics | Multicenter RCT in patients ≥2 years with acute uncomplicated UTI; satisfactory clinical response rates comparable between Cefprozil QD and cefaclor TID over 10 days |
| [7681376](https://pubmed.ncbi.nlm.nih.gov/7681376/) | 1993 | Systematic Review | Drugs | Comprehensive review of Cefprozil's antibacterial activity and therapeutic profile; confirms clinically relevant spectrum against E. coli, Klebsiella, and other Enterobacteriaceae relevant to UTI |
| [1494237](https://pubmed.ncbi.nlm.nih.gov/1494237/) | 1992 | Clinical Study (Pediatric) | Jpn J Antibiotics | Pediatric PK study with multiple doses; measured serum and urinary concentrations confirming adequate urinary drug levels for UTI coverage |
| [1289583](https://pubmed.ncbi.nlm.nih.gov/1289583/) | 1992 | Clinical Study (Pediatric) | Jpn J Antibiotics | 21 pediatric patients with bacterial infections including 3 UTI cases; good-to-excellent clinical response in 19/21 patients with complete bacterial eradication |
| [8464648](https://pubmed.ncbi.nlm.nih.gov/8464648/) | 1993 | Drug Review | Pediatric Annals | Review of Cefprozil's oral bioavailability, PK characteristics, and tolerability; confirms potential role in UTI management alongside respiratory and skin infections |
| [8042575](https://pubmed.ncbi.nlm.nih.gov/8042575/) | 1994 | Review | Am Family Physician | Comparative review of newer oral cephalosporins; Cefprozil confirmed as effective (though costly) alternative for skin, respiratory, and urinary tract infections with convenient dosing |
| [8529432](https://pubmed.ncbi.nlm.nih.gov/8529432/) | 1995 | In Vitro Study | Chemotherapy | Taiwan-based in vitro study on 637 clinical isolates; Cefprozil inhibited >80% of E. coli and K. pneumoniae at 8 mg/L — directly supports local uropathogen coverage |

---

## Taiwan Market Information

Cefprozil is currently **not registered** in Taiwan (TFDA). No product licenses, approved indications, or dosage forms are on file. For reference, Cefprozil is marketed in the United States under the brand name **Cefzil** and holds FDA approval for UTI, pharyngitis/tonsillitis, acute bronchitis, acute bacterial exacerbation of chronic bronchitis, and uncomplicated skin/soft tissue infections.

---

## Safety Considerations

Safety data (warnings, contraindications, drug-drug interactions) was not retrievable from the local TFDA database, as Cefprozil is not registered in Taiwan, and no DDI records were identified through available databases.

Please refer to the US FDA-approved prescribing information (Cefzil label) for full safety information, including guidance on penicillin/cephalosporin hypersensitivity, *Clostridioides difficile*-associated diarrhea risk, and use in renal impairment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three independent comparative RCTs — conducted across multiple centers, enrolling over 200 patients — consistently demonstrate that Cefprozil achieves clinical and bacteriological cure rates in acute uncomplicated UTI that are statistically equivalent to the reference standard cefaclor (~93–94%). The mechanistic basis is solid (PBP inhibition, high urinary drug concentrations, direct activity against E. coli, Klebsiella, and Proteus), and the indication is already approved by the US FDA. The primary barrier is the absence of Taiwan TFDA registration, not a lack of clinical evidence.

**To proceed, the following is needed:**

- **Regulatory pathway assessment**: Determine whether to pursue a new TFDA drug license application or rely on import for specific patient populations
- **Full safety dossier**: Obtain the FDA-approved US prescribing information (Cefzil label) for complete warnings, contraindications, and drug interaction data
- **Local resistance surveillance review**: Evaluate Taiwan AMR surveillance data (TSAR programme) to confirm that contemporary local E. coli and Klebsiella susceptibility rates remain adequate for empiric UTI treatment
- **Updated clinical evidence**: All available RCTs are from 1991–1995; a gap analysis should assess whether newer comparative data or guideline endorsements exist
- **Renal dosing guidance**: Confirm dose-adjustment protocols for patients with renal impairment, which is critical for UTI patients who often have underlying renal comorbidities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

