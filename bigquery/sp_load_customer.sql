CREATE OR REPLACE PROCEDURE `project.dataset.sp_load_customer`()
BEGIN
  INSERT INTO `project.dataset.customer_summary`
  SELECT
      customer_id,
      COUNT(*) AS transaction_count,
      SUM(amount) AS total_amount
  FROM `project.dataset.transactions`
  GROUP BY customer_id;
END;
