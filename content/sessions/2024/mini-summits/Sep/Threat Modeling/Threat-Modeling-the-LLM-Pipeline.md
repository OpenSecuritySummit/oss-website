---
title        : Threat Modeling the LLM Pipeline
track        : Threat Modeling
project      : Threat Modeling
type         : working-session
topics       : 
featured     :
event        : mini-summit
when_year    : 2024
when_month   : Sep
when_day     : Mon
when_time    : WS-16-17
hey_summit   : https://us06web.zoom.us/meeting/register/tZ0pd--vqDMpHdb22y_ipx7lNs4BwxFhokzI
session_slack:
#status      : draft
description  :
banner       : https://media.licdn.com/dms/image/v2/D4D22AQGaza2A1uBcVw/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1725395698367?e=2147483647&v=beta&t=75_8Cngo7Wfv8_1xl7aRaHooiloL6kQc2n4GEo69r5I
organizers   :
     - Brandon Green
    
youtube_link : 
zoom_link    : https://us06web.zoom.us/meeting/register/tZ0pd--vqDMpHdb22y_ipx7lNs4BwxFhokzI
---

## About this session
Rapid advancements in AI technologies have opened up a plethora of opportunities, but they’ve also introduced significant risks and challenges. One crucial yet often overlooked aspect of AI development is threat modeling. Threat modeling AI systems gives companies an edge in secure by design principles. This session aims to illuminate these potential threats within the AI pipeline and provides strategies for identifying, analyzing, and mitigating them.

### Presentation Outline: Threat Modeling the AI Pipeline

1. Introduction: What is Threat Modeling?

2. Data Collection:
What can go wrong? (Bias, poisoning)
Mitigations (Diversity in data sources, constant quality checks, skepticism about data origins)
Real-world examples (Amazon hiring algorithm, healthcare biases)

3. Data Preparation:
What can go wrong? (Privacy violations, feature engineering errors)
Mitigations (Data validation, encryption, regular audits, ongoing monitoring)

4. Learning Algorithm:
What can go wrong? (Overfitting, inadequate training)
Mitigations (Choose fair algorithms, diverse perspectives in development, ongoing monitoring)

5. Performance Evaluation:
What can go wrong? (Bias, data drift, etc.)
Mitigations (Cross-validation, data augmentation/diversification, fairness metrics, ongoing monitoring)

6. Deployment Considerations:
What can go wrong? (Cybersecurity threats)
Mitigations (Standard cybersecurity best practices)

7. User Input:
What can go wrong? (Prompt injections, misalignment)
Mitigations (Artful abstraction, contextual input handling, train for robustness, ongoing monitoring)
Real-world example (Bing Chat "Sydney")

8. Model Output:  
What can go wrong? (Bias, misinformation)
Mitigations (Fact-checking, authenticity mechanisms, limit access, ongoing monitoring)

9. Fully Trained Model:
What can go wrong? (Adversarial attacks, model drift)
Mitigations (Adversarial training, encourage good behavior, ongoing monitoring)

10. Conclusion: Building Responsible AI
