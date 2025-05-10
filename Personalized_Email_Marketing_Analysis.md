# The Impact of Personalized Email Marketing on Customer Engagement

## Introduction

In the evolving digital landscape, email marketing remains a cornerstone strategy for businesses aiming to connect with customers in a targeted and measurable way. Amidst the growing number of marketing channels, personalized email marketing has gained prominence for its ability to deliver tailored content that resonates with individual recipients. By leveraging customer data such as past purchases, browsing behavior, and demographic information, personalized emails can foster stronger relationships, increase open and click-through rates, and ultimately drive higher conversion rates. This approach aligns with the growing consumer expectation for more relevant and meaningful interactions with brands. Moreover, as customers become increasingly selective about the content they engage with, relevance becomes a critical driver of brand loyalty and long-term customer value.

This research investigates the effects of personalized email marketing on customer engagement through an A/B testing framework, comparing the effectiveness of personalized versus generic email content. The findings aim to provide insights into how data-driven personalization strategies can enhance digital marketing performance and customer satisfaction. In addition to basic engagement metrics, the study also considers how personalization may influence customer perception of brand authenticity and trustworthiness, which are essential for sustainable business growth in competitive online environments.

The primary objective is to determine whether personalization enhances engagement metrics; such as open rates, click-through rates, and unsubscribe rates compared to non-personalized email communications. The research hypothesis is structured as follows:

H₀: Personalized emails do not significantly affect customer engagement.
H₁: Personalized emails significantly increase customer engagement.

This study responds to the increasing demand for data-driven marketing strategies, particularly those that can be empirically validated and scaled using automation tools. As competition intensifies, businesses are required to optimise their customer communication strategies not only for efficiency but also for relevance and responsiveness (Rana et al., 2024). Personalized email marketing leverages customer data such as browsing behaviour, purchase history, and demographic attributes to craft highly relevant content, thereby improving the likelihood of engagement (Verma and Fatma, 2025).

Previous empirical studies suggest that such personalization enhances the perceived value of messages, leading to improved customer satisfaction and increased interaction rates (Sayeed, 2023; Wang, Lu and Shi, 2022). By conducting a rigorous A/B testing experiment, this research aims to build on these findings and provide actionable insights into how personalized email marketing can be strategically implemented to improve engagement outcomes and support long-term digital marketing effectiveness.

## Methodology

### Experimental Design

This study employed an A/B testing framework to assess the effectiveness of personalized versus generic email marketing strategies. Participants were randomly divided into two groups to eliminate selection bias and enhance the validity of the results. The experiment was conducted using Mailchimp, a widely used email marketing platform that facilitated accurate audience segmentation, automated delivery, and real-time performance tracking. A multivariate test focusing specifically on subject lines was carried out to evaluate how personalized versus generic subject lines influenced key engagement metrics such as open rates and click-through rates. By isolating subject lines as the variable, the study aimed to determine the direct impact of personalization at the first point of customer interaction.

Group A received emails that were personalized based on recipient-specific attributes such as name, previous interaction history, and segmented interests.

Group B received standard, non-personalized (generic) emails with identical content for all recipients.

Each group consisted of approximately 95 recipients, yielding a total sample size of around 190 individuals. The emails were dispatched using the professional aforementioned email marketing platform that supports A/B testing and real-time analytics. This platform enabled precise tracking of various key performance indicators (KPIs), including open rate, click-through rate (CTR), bounce rate, and unsubscribe rate.

The data collected from the email campaign were exported in .csv format, allowing for structured data management and analysis. Python was employed for both data visualization and inferential statistical analysis. Libraries such as pandas were used for data cleaning and manipulation, while matplotlib and seaborn facilitated the generation of graphical insights, including bar charts and line graphs for comparative trends.

For inferential statistics, scipy.stats and statsmodels libraries were utilized to conduct t-tests and calculate confidence intervals, enabling the identification of statistically significant differences between the two groups. This rigorous methodology ensured that any observed effect on engagement metrics could be attributed with greater confidence to the email personalization variable.

### Email Content

- **Personalized Email**: Included customer names and recommendations (e.g., “Hi [Name], we think you’ll love these items!”).
- **Generic Email**: A standard promotional message (e.g., “Check out our latest collection!”).

### Data Collected

| Group | Email Type   | Total Recipients | Successful Deliveries | Bounce Rate | Open Rate | Total Opens | Click Rate | Total Clicks | Unsubscribe Rate | Total Unsubs |
|-------|--------------|------------------|------------------------|-------------|-----------|--------------|------------|---------------|-------------------|--------------|
| A     | Personalized | 95               | 93                     | 2.10%       | 31.20%    | 54           | 0.00%      | 0             | 0.00%             | 0            |
| B     | Generic      | 94               | 91                     | 3.20%       | 19.80%    | 21           | 0.00%      | 0             | 1.10%             | 1            |

## Results
# Insight into Campaign Performance
The comparative analysis of email campaign Group A (Personalized) and Group B (Generic) reveals a substantial difference in customer engagement metrics. Group A achieved an open rate of 31.2%, while Group B recorded a significantly lower 19.8%. Despite similar numbers of successful deliveries (93 vs. 91), the personalized email group demonstrated notably higher engagement, suggesting that tailored content substantially increases the likelihood of recipients opening emails.

Bounce rates were also slightly lower in Group A (2.10%) compared to Group B (3.20%), indicating better deliverability possibly linked to increased sender reputation through personalization practices (Rana, Kiran and Gul, 2024). Importantly, the unsubscribe rate in Group A was 0.00%, in contrast to Group B’s 1.10%, highlighting higher message relevance and recipient satisfaction for the personalized group.

Although neither group recorded any clicks, likely due to either content layout or audience readiness, the overall insights support existing research that personalized communications increase engagement and reduce opt-outs (Verma and Fatma, 2025; Sayeed, 2023). These findings reinforce the effectiveness of personalization as a strategic tool in digital marketing and align with previous studies linking tailored content to enhanced user response (Wang, Lu and Shi, 2022).
### Data Visualization

**Figure 1: Engagement Metrics**
![engagement_metrics_comparison](https://github.com/user-attachments/assets/13b3f2af-58aa-45fe-ab16-f6f1e794d0bb)

The open rate for personalized emails (31.2%) is significantly higher than for generic emails (19.8%). Meanwhile, the unsubscribe rate is higher in the generic group (1.1%) compared to 0% in the personalized group.



**Figure 2: Comparison Engagement Metrics**
![Comparison of Engagement Metrics](Charts/Comparison%20engagment%20Metrics.png)


**Figure 3: Engage Metrics Breakdown**
![Engagement Metrics Breakdown](Charts/Engagement%20Metrics%20Breakdown.png)


**Figure 4: Key Metric Comparison**
![Key Metric Comparison](Charts/Key%20Metric%20Comparison.png)


**Figure 5: Open Rate Contingency Table**
![Open Rate Contingency Table](Charts/Open%20Rate%20Contingency%20table.png)



### Statistical Analysis

📐 Table 2: Summary of Inferential Statistics (Two-Proportion Z-Test)
| **Statistics**               | **Value**                                               |
|--------------------------|----------------------------------------------------------|
| Z-statistic              | 4.176                                                    |
| P-value                  | 0.000 (rounded; actual ≈ 0.000015)                       |
| Alpha level              | 0.05                                                     |
| Statistical significance | Yes (p < 0.05)                                           |
| Conclusion               | Reject H₀ – Personalized emails significantly increased customer engagement |


I performed a two-proportion z-test to evaluate the significance of the difference in open rates:

- **Group A (Personalized)**: 54 opens out of 93
- **Group B (Generic)**: 21 opens out of 91

The A/B test analysis revealed a statistically significant difference in customer engagement between personalized and generic email campaigns. With a Z-statistic of 4.176 (p=0.000), the results exceeded the predetermined alpha threshold of α=0.05, leading to the rejection of the null hypothesis (H_0). This indicates that the observed improvement in open rates for personalized emails is unlikely to be due to random chance. The Z-score of 4.176 reflects that the personalized email group’s performance (31.2% open rate) was 4.176 standard errors above the expected mean under H₀, with a standard error of approximately 0.0273, providing robust evidence for the alternative hypothesis (H_1).

The p-value of 0.000 signifies only a 0% probability of observing such a disparity if no true effect existed. Personalized emails achieved a 57% relative increase in open rates compared to generic emails (31.2% vs. 19.8%), demonstrating both statistical and practical significance. This aligns with empirical studies emphasizing personalization’s role in enhancing customer engagement. While the results confirm the efficacy of tailored content for improving open rates, the absence of clicks (0% CTR in both groups) suggests further optimization of email content or calls-to-action is necessary.

These findings showed the value of personalization in email marketing strategies, though future research should explore long-term engagement and conversion impacts. The analysis validates the hypothesis that personalized emails drive meaningful engagement, offering actionable insights for businesses aiming to refine their digital marketing approaches.


## Discussion

The findings of this A/B test align with empirical research demonstrating that personalised email marketing significantly enhances customer engagement. Studies by Verma and Fatma (2025) and Sayeed (2023) posit that tailored content increases perceived relevance, thereby improving open rates and reducing opt-outs. This is evident in the 57% higher open rate for Group A (31.2%) compared to Group B (19.8%), reinforcing the notion that personalisation fosters a stronger connection with recipients. The absence of clicks in both groups, however, suggests limitations in content design or calls-to-action (CTAs), underscoring the need for complementary strategies such as dynamic visuals or urgency-driven messaging (Valenzuela-Gálvez et al., 2022).

Advanced technologies like AI-driven segmentation and predictive analytics could further optimise engagement. For instance, Ijomah et al. (2024) highlight that machine learning algorithms enable hyper-targeted campaigns by analysing behavioural data, which could address the CTR gap observed in this study. Similarly, Deligiannis et al. (2020) demonstrate that timing optimisation sending emails when users are most active can amplify open rates. Integrating these tools could refine personalisation strategies beyond basic name inclusion, such as tailoring product recommendations based on browsing history or past purchases.

Ethical considerations remain critical. Rahayu et al. (2025) caution that overly intrusive personalisation may erode trust, particularly if users perceive excessive data usage. Transparent consent mechanisms and clear privacy policies, as recommended by Wang et al. (2022), are essential to mitigate such risks. This study’s low unsubscribe rate in Group A (0%) supports this approach, indicating that ethical personalisation balances relevance with respect for user autonomy.

Practically, businesses should adopt a phased implementation of personalisation tools. Starting with basic segmentation (e.g., demographics) before progressing to AI-driven methods allows organisations to test efficacy while managing costs. Additionally, A/B testing different levels of personalisation (e.g., name-only vs. full behavioural tailoring) could identify optimal strategies for specific audiences.

Thus, while personalisation is empirically validated as effective, its success hinges on strategic implementation, technological integration, and ethical data practices. Future research should explore long-term engagement impacts and cross-cultural variations in response to personalised content

## Conclusion

This study conclusively demonstrates that personalised email marketing significantly enhances customer engagement, with Group A achieving a 31.2% open rate compared to 19.8% for generic emails. The statistical significance of these results (Z = 4.176, p = 0.000) robustly supports the alternative hypothesis (H₁), aligning with prior research by Rana et al. (2024) and Verma and Fatma (2025). The 57% relative improvement in open rates underscores personalisation’s potential to cut through digital clutter, while the absence of unsubscribes in Group A highlights its role in sustaining recipient satisfaction.

However, the lack of clicks in both groups reveals a critical gap: personalisation alone cannot drive conversions without compelling content. Businesses must pair tailored messaging with strong CTAs, visually engaging designs, and time-sensitive offers to maximise impact. Integrating AI tools for advanced segmentation and predictive analytics, as proposed by Ijomah et al. (2024), could further refine targeting and timing.

Ethical considerations are equally vital. Transparent data practices, as emphasised by Rahayu et al. (2025), ensure compliance with privacy regulations and foster long-term trust. Organisations should prioritise consent-driven personalisation and avoid over-reliance on sensitive data.

For practitioners, the key takeaway is to adopt a balanced approach: leverage personalisation to boost engagement while investing in content quality and ethical frameworks. Future research should investigate longitudinal effects of personalisation on customer lifetime value and explore its efficacy in diverse cultural contexts. Ultimately, this study affirms that personalised email marketing, when executed strategically, is a powerful tool for enhancing digital engagement in competitive markets.

### Implications

- Businesses should implement AI-powered personalization to increase campaign ROI.

  Integrating AI into marketing allows businesses to analyze behavior, predict optimal send times, and personalize at scale. This improves ROI by making campaigns more        relevant and efficient.

- Ethical data handling practices must be adopted to ensure long-term trust.

  Personalization must be grounded in transparency. Clear communication about data use, user control over preferences, and GDPR compliance are essential for maintaining       consumer trust and avoiding backlash.

- Marketing teams should adopt a test-and-learn approach to personalization.

  Start with simple tactics like using names, then scale up using behavioral data. A/B testing helps identify what resonates best, allowing for continuous refinement and      reduced risk.

- Content quality must complement personalization to drive action.

  A personalized subject line can boost opens, but compelling visuals, CTAs, and value-driven messaging are critical to drive conversions and click-throughs.

- Cross-functional collaboration enhances implementation of personalization strategies.

  Effective personalization involves marketers, data scientists, designers, and legal teams working together to create campaigns that are creative, technically sound, and     privacy-compliant.

- Future research should evaluate long-term effects and broader customer metrics.

## References

Deligiannis, A., Argyriou, C. and Kourtesis, D. (2020) ‘Predicting the optimal date and time to send personalized marketing messages to repeat buyers’, *International Journal of Advanced Computer Science and Applications*, 11(4). www.ijacsa.thesai.org

Ijomah, T., Idemudia, C., Eyo-Udo, N. and Anjorin, K. (2024) ‘Innovative digital marketing strategies for SMEs: driving competitive advantage and sustainable growth’, *International Journal of Management & Entrepreneurship Research*, 6(7), pp. 2173–2188. https://fepbl.com/index.php/ijmer/article/view/1265

Rahayu, T., Purnamasari, V., Rizky, M., Rahyadi, I. and Mani, L. (2025) ‘Feeling watched: a phenomenological exploration of consumer discomfort and data privacy concerns in e-commerce personalized email marketing’, *PaperASIA*, 41(1b), pp. 81–92. https://doi.org/10.59953/paperasia.v41i1b.313.

Rana, R., Kiran, S. and Gul, S. (2024) ‘The impact of email marketing on consumer buying decision process in the Pakistani market’, *Journal for Business Education and Management*, 4(1), pp. 209–226. https://doi.org/10.56596/jbem.v4i1.24.

Sayeed, D. (2023) ‘Email marketing – role in improving customer retention rates’, *EPRA International Journal of Economics Business and Management Studies*, pp. 95–99.https://eprajournals.com/IJHS/article/10150/abstract

Verma, S. and Fatma, S. (2025) ‘How personalization and AI are transforming digital marketing campaigns’, *International Journal of Scientific Research in Engineering and Management*, 9(3), pp. 1–9. https://ijsrem.com/download/how-personalization-and-ai-are-transforming-digital-marketing-campaigns/

Wang, Y., Lu, L. and Shi, P. (2022) ‘Does customer email engagement improve profitability? Evidence from a field experiment in subscription service retailing’, *Manufacturing & Service Operations Management*, 24(5), pp. 2703–2721. https://pubsonline.informs.org/doi/10.1287/msom.2022.1122.
