-- Customer transaction summary
SELECT
    customer_id,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM `project.dataset.transactions`
GROUP BY customer_id;
