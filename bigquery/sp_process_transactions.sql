CREATE OR REPLACE PROCEDURE `project.dataset.sp_process_transactions`()
BEGIN
  CREATE OR REPLACE TABLE `project.dataset.processed_transactions` AS
  SELECT
      transaction_id,
      customer_id,
      SAFE_CAST(amount AS NUMERIC) AS amount,
      SAFE_CAST(transaction_timestamp AS TIMESTAMP) AS transaction_timestamp
  FROM `project.dataset.raw_transactions`
  WHERE transaction_id IS NOT NULL;
END;
