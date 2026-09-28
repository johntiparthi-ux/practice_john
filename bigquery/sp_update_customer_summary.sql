CREATE OR REPLACE PROCEDURE `project.dataset.sp_update_customer_summary`()
BEGIN
  MERGE `project.dataset.customer_summary` T
  USING (
    SELECT
      customer_id,
      COUNT(*) AS transaction_count,
      SUM(amount) AS total_amount
    FROM `project.dataset.transactions`
    GROUP BY customer_id
  ) S
  ON T.customer_id = S.customer_id
  WHEN MATCHED THEN
    UPDATE SET
      transaction_count = S.transaction_count,
      total_amount = S.total_amount
  WHEN NOT MATCHED THEN
    INSERT (customer_id, transaction_count, total_amount)
    VALUES (S.customer_id, S.transaction_count, S.total_amount);
END;
