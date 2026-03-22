LOAD CSV FROM 'file:///'
AS row
MERGE (:Paper {
  id: row.id,
  title: row.title,
  journal_ref: row.journal-ref,
  doi: row.doi,
  report_no: row.report-no,
  categories: row.categories,
  license: row.license,
  abstract: row.abstract,
  latest_version_number: row.latest_version_number,
  latest_version_date: row.latest_version_date
})