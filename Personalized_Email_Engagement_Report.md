
# The Impact of Personalized Email Marketing on Customer Engagement

## Introduction

Personalized marketing is increasingly leveraged by companies to foster stronger customer relationships and increase engagement metrics such as open rates, click-through rates (CTR), and conversions. This project investigates the effectiveness of personalized versus generic email marketing through an A/B testing approach. 

**Research Question**:  
Does personalized email marketing significantly improve customer engagement compared to generic email campaigns?

**Hypotheses**:  
- **Null Hypothesis (H₀)**: Personalized emails do not significantly affect customer engagement.  
- **Alternative Hypothesis (H₁)**: Personalized emails significantly increase customer engagement.

## Methodology

This study utilized an A/B test design to evaluate customer engagement based on email type.

### Experimental Design

- **Independent Variable**: Type of Email  
  - **Personalized**: Emails included the customer’s name and tailored offers.  
  - **Generic**: Emails contained standard promotional content without personalization.

- **Dependent Variables**:  
  - Open Rate (Total Opens / Successful Deliveries)  
  - Click-Through Rate (CTR) (Total Clicks / Successful Deliveries)  
  - Conversion Rate (Not observed in this dataset)

### Data Overview

The dataset included 200 samples, with the following aggregate summary:

| Email Type   | Total Opens | Total Clicks | Successful Deliveries | Open Rate | CTR  |
|--------------|-------------|--------------|------------------------|-----------|------|
| Personalized | 54          | 0            | 93                     | 0.58      | 0.00 |
| Generic      | 21          | 0            | 91                     | 0.23      | 0.00 |

## Results

### Engagement Dashboard

![email_engagement_dashboard](https://github.com/user-attachments/assets/8f342087-de01-491f-910d-88ea5b59d688)


### Key Observations

- **Open Rate**: Personalized emails achieved an open rate of 58%, significantly higher than the 23% of generic emails.
- **Click-Through Rate**: No clicks were recorded in either group, indicating room for improvement in content strategy.
- **Deliverability**: Both groups had high and nearly equal successful delivery rates.

### Statistical Test

Due to binary grouping and continuous proportion (open rates), a **two-proportion z-test** was conducted.

- z-score ≈ 4.10
- p-value < 0.001

**Interpretation**: The difference in open rates between personalized and generic emails is statistically significant. Therefore, we reject the null hypothesis (H₀).

## Discussion

Our findings support the assertion that personalization in email marketing positively affects customer engagement, particularly in open rates. This aligns with literature highlighting the psychological impact of personalization:

- **Chaffey & Smith (2017)** emphasize that personalization increases perceived relevance and trust.
- **Kotler & Keller (2016)** suggest that name-based personalization significantly boosts attention in marketing communication.
- **Jain et al. (2020)** demonstrated improved ROI in personalized campaigns in e-commerce.
- **Lacy & Dowling (2021)** report that engagement rates improve up to 60% in B2C campaigns with targeted messaging.
- **Kumar et al. (2019)** found personalization leads to higher loyalty metrics in omnichannel strategies.

### Limitations

- No conversions or clicks were recorded, limiting analysis to open rate.
- The test did not control for time of sending or subject line consistency.
- Results are limited by sample size and lack of demographic segmentation.

## Conclusion

Personalized email marketing significantly improves open rates compared to generic email campaigns, confirming the hypothesis that tailored content enhances customer engagement. Despite limitations, this study provides evidence-based insights for marketers aiming to improve campaign performance through personalization.

## Real-World Applications

- Marketing teams can increase open rates by including customer names and tailored content.
- A/B testing frameworks should be embedded into email automation systems.
- Further analysis should track downstream metrics like conversions and lifetime value.
