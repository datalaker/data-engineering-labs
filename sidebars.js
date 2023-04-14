/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docs: [
    'introduction',
    {type: 'category', label: 'Getting Started', items: [
      {type: 'category', label: 'Data Engineering', items: [
      'foundations/basics/de-basics',
      'foundations/basics/data-pipelines',
      'foundations/basics/oltp-vs-olap',
      'foundations/basics/data-storages',
      'foundations/basics/sql-vs-nosql',
      'foundations/basics/big-data',
      'foundations/basics/batch-vs-incremental',
      'foundations/basics/data-contract',
      'foundations/basics/data-governance',
      'foundations/basics/data-management',
      'foundations/basics/data-quality',
      'foundations/basics/batch-data-processing',
      'foundations/basics/stream-data-processing',
      'foundations/basics/most-common-interview-questions-set1',
      'foundations/basics/most-common-interview-questions-set2',
      'foundations/basics/most-common-interview-questions-set3',
      ]},
      {type: 'category', label: 'Spark and Hadoop', items: [
        'foundations/basics/spark-basics',
        'foundations/basics/spark-origin',
        'foundations/basics/hadoop-basics',
        'foundations/basics/map-reduce',
        'foundations/basics/hadoop-vs-spark',
        'foundations/basics/spark-dag',
        'foundations/basics/rdd',
        'foundations/basics/spark-quiz',
        ]},
        {type: 'category', label: 'Developer Essentials', items: [
          'foundations/developer/install-anaconda',
          'foundations/developer/install-jupyter',
          'foundations/developer/install-vscode',
          'foundations/developer/lab-explore-vscode-features',
          'foundations/developer/setup-git',
          'foundations/developer/lab-learn-git-commands',
          'foundations/developer/lab-bash-commands/index',
          'foundations/developer/install-dbeaver',
          ]},
    ]},
    {type: 'category', label: 'Cloud Computing', items: [
      {type: 'category', label: 'Introduction', items: [
      'foundations/cloud/cloud-basics',
      'foundations/cloud/cloud-comparison',
      ]},
      {type: 'category', label: 'AWS', items: [
        'foundations/cloud/ec2',
        'foundations/cloud/iam',
        'foundations/cloud/glue',
        'foundations/cloud/rds',
        'foundations/cloud/s3',
        'foundations/cloud/dms',
        'foundations/cloud/secrets-manager',
        'foundations/cloud/aws-containers',
        'foundations/cloud/aws-commands',
        'foundations/cloud/lab-aws-setup/README',
        'foundations/cloud/lab-create-iam-policy-role/README',
        'foundations/cloud/lab-aws-secrets-manager/README',
        'foundations/cloud/lab-create-your-first-vpc/README',
        'foundations/cloud/lab-create-your-first-ec2-instance-linux/README',
        ]},
        {type: 'category', label: 'GCP', items: [
          'foundations/cloud/gcp-basics',
          'foundations/cloud/gcp-setup',
          ]},
        {type: 'category', label: 'Azure', items: [
          'foundations/cloud/azure-basics',
          'foundations/cloud/azure-data-ingestion',
          'foundations/cloud/azure-batch-processing',
          'foundations/cloud/azure-fullstack-solutions',
          ]},
    ]},
    {type: 'category', label: 'Programming', items: [
      {type: 'category', label: 'SQL', items: [
      'foundations/language/sql/sql-basics',
      'foundations/language/sql/sql-query',
      'foundations/language/sql/commands/index',
      'foundations/language/sql/cte',
      'foundations/language/sql/subquery',
      'foundations/language/sql/views',
      'foundations/language/sql/stored-procedures',
      'foundations/language/sql/triggers',
      'foundations/language/sql/indexes',
      'foundations/language/sql/comparison-operators',
      'foundations/language/sql/logical-operators',
      'foundations/language/sql/joins',
      'foundations/language/sql/comments',
      'foundations/language/sql/cursor',
      'foundations/language/sql/aggregate-functions',
      'foundations/language/sql/string-functions',
      'foundations/language/sql/date-functions',
      'foundations/language/sql/window-functions',
      'foundations/language/sql/performance-tuning',
      'foundations/language/sql/joins',
      'foundations/language/sql/lab-mysql-data-ingestion/index',
      'foundations/language/sql/lab-basic-to-advanced/index',
      'foundations/language/sql/lab-postgres-queries/index',
      'foundations/language/sql/lab-postgres-sales/index',
      'foundations/language/sql/lab-sqlite-basics/index',
      'foundations/language/sql/challenges/yammer/index',
      'foundations/language/sql/challenges/braintree/index',
      'foundations/language/sql/challenges/employee',
      'foundations/language/sql/challenges/assignment5/index',
      'foundations/language/sql/links'
      ]},
    ]},
  ],
};

module.exports = sidebars;
