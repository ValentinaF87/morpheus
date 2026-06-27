# Morpheus Architecture

## Overview

Morpheus is composed of a sequence of AI-assisted workflows that transform incoming opportunities into structured recommendations and continuously collect feedback to improve future evaluations.

```
                Gmail
                   │
                   ▼
        LinkedIn Job Alert Email
                   │
                   ▼
          Job Extraction Workflow
                   │
                   ▼
      LinkedIn Job Description Retrieval
                   │
                   ▼
             AI Job Evaluation
                   │
                   ▼
        Recommendation Generation
                   │
                   ▼
         Telegram Notification
                   │
                   ▼
           Human Decision
                   │
                   ▼
         Human Feedback Dataset
```

---

## Current Components

### Gmail Ingestion

Receives incoming LinkedIn job alert emails.

---

### Job Extraction

Splits emails containing multiple opportunities into individual job items.

---

### Job Retrieval

Retrieves the complete job description from LinkedIn.

---

### AI Evaluation

Evaluates each opportunity against a configurable profile and produces:

- recommendation
- match score
- explanation

---

### Notification Layer

Sends concise Telegram summaries to support quick decision making.

---

### Feedback Collection

Stores both AI recommendations and human decisions for future analysis.

---

## Current Storage

Today Morpheus uses Google Sheets as lightweight storage for:

- processed opportunities
- deduplication
- human feedback

This choice prioritizes simplicity over scalability.

Future versions will migrate to a proper database.

---

## Future Evolution

The next architectural milestone is introducing a feedback analytics layer capable of measuring AI performance and identifying improvement opportunities.
