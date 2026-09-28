-- Incremental load using a watermark
SELECT *
FROM `project.dataset.transactions`
WHERE transaction_timestamp > @last_watermark;
