---
layout: default
title: Bismuth Subsalicylate
parent: 僅模型預測 (L5)
nav_order: 462
evidence_level: L5
indication_count: 10
---

# Bismuth Subsalicylate
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

# Bismuth Subsalicylate: From Gastrointestinal Disorders to Paratyphoid Fever

## One-Sentence Summary

Bismuth subsalicylate (BSS), the active ingredient in Pepto-Bismol, is a widely used over-the-counter agent for gastrointestinal disorders including traveler's diarrhea, dyspepsia, and adjunctive *H. pylori* eradication.
The TxGNN model predicts it may be effective for **Paratyphoid Fever** (highest-ranked among 10 predicted indications, score 99.98%), with the closely related indication of **salmonellosis** (rank 3) representing the best-evidenced candidate, supported by **6 publications** including an in vitro bactericidal study and multiple clinical reviews.
No clinical trials have been registered for any of the 10 predicted indications, placing this candidate at an early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | OTC antidiarrheal / GI disorders (traveler's diarrhea, dyspepsia) |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Market Status | Not registered in Taiwan (0 licenses) |
| Number of NDAs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Bismuth subsalicylate exerts its effects through two complementary mechanisms. The bismuth component binds directly to bacterial lipopolysaccharide (LPS) on gram-negative cell membranes, disrupting membrane integrity and killing the organism — an effect confirmed in vitro against *Escherichia coli*, *Salmonella* spp., and other enteric pathogens (Sox & Olson, 1989). Separately, the salicylate moiety inhibits cAMP-mediated intestinal chloride secretion, reducing fluid loss and diarrheal output by approximately 50% regardless of pathogen identity.

Paratyphoid fever is caused by *Salmonella enterica* serovars Paratyphi A, B, and C — placing it squarely within the *Salmonella* genus where BSS's LPS-binding bactericidal activity has been mechanistically established. This explains why TxGNN assigns the highest prediction score to paratyphoid fever: the knowledge graph infers a strong path from BSS → anti-*Salmonella* activity → *Salmonella*-caused systemic febrile illness.

However, a critical pharmacokinetic limitation must be acknowledged. Unlike non-typhoidal *Salmonella* gastroenteritis (confined to the intestinal lumen), paratyphoid fever is a **systemic bacteremic infection**. BSS is poorly absorbed after oral administration, with its antibacterial effect largely restricted to the intestinal lumen. It cannot achieve therapeutic bismuth concentrations in blood, liver, or lymph nodes where *Salmonella* Paratyphi resides during bacteremia. Therefore, BSS is not a candidate to replace fluoroquinolone or third-generation cephalosporin therapy for paratyphoid fever, but may theoretically contribute to intestinal decolonization as an adjunct — a role that remains entirely unproven.

---

## Clinical Trial Evidence

Currently no clinical trials related to paratyphoid fever have been registered for bismuth subsalicylate.

---

## Literature Evidence

Currently no literature directly addressing bismuth subsalicylate in paratyphoid fever is available.

The mechanistically related indication **salmonellosis** (TxGNN rank 3, score 99.95%) does have supporting literature; these publications underpin the plausibility of the paratyphoid fever prediction via shared *Salmonella* biology:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2694949](https://pubmed.ncbi.nlm.nih.gov/2694949/) | 1989 | In vitro mechanistic | Antimicrob Agents Chemother | BSS binds and kills diverse gram-negative bacteria; 4-log₁₀ reduction of viable cells within 4 h; binding is concentration- and inoculum-dependent |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | Am J Med | BSS reduces stool number by ~50% in acute enteric infections; antisecretory mechanism independent of pathogen identity |
| [6385704](https://pubmed.ncbi.nlm.nih.gov/6385704/) | 1984 | Review | Am J Med Sci | Traveler's diarrhea overview; BSS cited as effective non-antibiotic option covering Salmonella-associated TD |
| [2258602](https://pubmed.ncbi.nlm.nih.gov/2258602/) | 1990 | Review | Infect Control Hosp Epidemiol | Traveler preparation guidelines; BSS recommended alongside antibiotics for high-risk itineraries |
| [2655632](https://pubmed.ncbi.nlm.nih.gov/2655632/) | 1989 | Review | Annu Rev Public Health | Global diarrheal disease control; BSS role in resource-limited settings discussed |
| [1760758](https://pubmed.ncbi.nlm.nih.gov/1760758/) | 1991 | Animal study (veterinary) | Vet Clin North Am Food Anim Pract | BSS as antisecretory agent in neonatal calf salmonellosis; supports adjunctive intestinal role |

---

## Market Information

Bismuth subsalicylate has **no registered pharmaceutical products in Taiwan** (0 authorizations; query confirmed 2026-03-24). It is not approved through a prescription pathway in Taiwan.

In the United States, BSS is widely available as an OTC product (Pepto-Bismol and generic equivalents) for the symptomatic treatment of diarrhea, heartburn, indigestion, and upset stomach. It is also used as a component of *H. pylori* quadruple eradication regimens. No US prescription NDA data was included in this Evidence Pack.

---

## Safety Considerations

Formal package insert data for Taiwan is unavailable (product not registered). The following reflects established pharmacological knowledge for the US-marketed formulation:

- **Salicylate toxicity**: BSS contains salicylate. Should not be used in children or teenagers recovering from viral illnesses (influenza, chickenpox) due to Reye's syndrome risk. Avoid in patients with aspirin allergy or salicylate hypersensitivity.
- **Bismuth accumulation**: Prolonged use at high doses may cause bismuth encephalopathy (rare); short-course use at label doses is considered safe.
- **Drug interactions**: Bismuth may chelate and reduce absorption of tetracyclines and fluoroquinolones — separate administration by at least 2 hours. May potentiate anticoagulants (salicylate component).
- **Benign adverse effects**: Black discoloration of stool and tongue is expected (bismuth sulfide formation) and does not require discontinuation.

Please refer to the full US FDA-approved labeling for comprehensive safety information.

---

## Multi-Indication Overview

This candidate was evaluated across 10 predicted indications. The table below summarizes the full landscape:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Note |
|------|---------|-------------|----------------|----------------|----------|
| 1 | Paratyphoid fever | 99.98% | L4 | Research Question | Mechanistically sound; systemic infection limits oral BSS reach |
| 2 | Diffuse scleroderma | 99.96% | L5 | Hold | No mechanistic link; probable AI false positive via indirect KG path |
| **3** | **Salmonellosis** | **99.95%** | **L3** | **Proceed with Guardrails** | **Best-evidenced; 6 publications; indirect RCT support via traveler's diarrhea** |
| 4 | Typhoid fever | 99.92% | L4 | Research Question | Same systemic limitation as paratyphoid; adjunctive decolonization role plausible |
| 5 | Conjunctivitis | 99.92% | L5 | Hold | Ocular route not feasible; established topical antibiotics available |
| 6 | Relapsing fever | 99.85% | L5 | Hold | Historical spirochete link too indirect; doxycycline is effective standard of care |
| 7 | Acute contagious conjunctivitis | 99.84% | L5 | Hold | Same ocular route barrier; no data |
| 8 | Gingivitis | 99.75% | L4 | Research Question | 4 publications including in vitro nano-BSS against oral anaerobes; Vincent's angina historical use |
| 9 | Punctate epithelial keratoconjunctivitis | 99.74% | L5 | Hold | Viral/dry-eye etiology; BSS mechanism irrelevant |
| 10 | Otitis externa | 99.68% | L5 | Hold | No otic formulation; acetic acid and fluoroquinolone ear drops are standard |

**Summary pattern**: TxGNN predictions cluster into (a) *Salmonella* / enteric infections — biologically coherent, evidence-supported; (b) ocular/ENT infections — route barriers make these non-viable; and (c) autoimmune/connective tissue diseases — probable false positives.

---

## Conclusion and Next Steps

**Decision: Research Question** *(for paratyphoid fever, top-ranked prediction)*

**Best Actionable Opportunity: Proceed with Guardrails** *(for salmonellosis, rank 3 — most evidenced indication)*

**Rationale:**
For paratyphoid fever specifically, BSS's antibacterial mechanism is biologically plausible at the genus level, but the systemic nature of this infection and BSS's negligible oral bioavailability create a fundamental pharmacokinetic barrier that cannot be bridged without compelling new evidence. The prediction is worth investigating as a mechanistic question, not a clinical trial priority at this stage. For non-typhoidal salmonellosis (gastroenteritis form), BSS already has indirect clinical backing through traveler's diarrhea programs and confirmed in vitro bactericidal activity — making it the actionable lead from this analysis.

**To proceed (prioritized by indication):**

For **salmonellosis** (Proceed with Guardrails):
- Conduct a dedicated prospective trial or retrospective cohort study evaluating BSS adjunctive therapy in non-typhoidal Salmonella gastroenteritis
- Establish luminal bismuth concentrations achievable with standard OTC dosing against clinical Salmonella MIC distributions
- Obtain complete MOA data via DrugBank API (currently a data gap)

For **paratyphoid fever** (Research Question):
- Commission a targeted literature search for bismuth compounds in enteric fever adjunctive therapy
- Consult infectious disease specialists on whether intestinal decolonization endpoint is clinically meaningful in paratyphoid management

For **gingivitis** (Research Question, secondary):
- Advance BSS nanoparticle research to in vivo periodontal model before clinical translation
- Identify feasible oral delivery formulation (mouthwash, gel) distinct from current tablet/liquid forms

For all indications:
- Assess Taiwan regulatory pathway (import/clinical trial application) given zero local registrations
- Document safety plan distinguishing salicylate vs. bismuth toxicity monitoring endpoints
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

