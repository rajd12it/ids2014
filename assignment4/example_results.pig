register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

--load the test file into Pig
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
--later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-*' USING TextLoader as (line:chararray);
--parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);
--describe ntriples;
--group the n-triples by object column
--objects = group ntriples by (object) PARALLEL 50;
--subjects = group ntriples by (subject) PARALLEL 10;
subjects = GROUP ntriples BY (subject) PARALLEL 76;
--describe subjects;

--filtered = FILTER ntriples BY subject matches '.*business.*';
--filtered = FILTER ntriples BY subject matches '.*rdfabout\\.com.*';
--describe filtered;
--dump filtered;
--filtered_copy = FOREACH filtered GENERATE * AS (subject2:chararray,predicate2:chararray,object2:chararray);
--describe filtered_copy;
--dump filtered_copy;

--joined = JOIN filtered BY subject, filtered_copy BY subject2;
--joined = JOIN filtered BY object, filtered_copy BY subject2;
--describe joined;
--dump joined;
--distinct_joined = DISTINCT joined PARALLEL 10;
--describe distinct_joined;
--dump distinct_joined;

--flatten the objects out (because group by produces a tuple of each object
--in the first column, and we want each object to be a string, not a tuple),
--and count the number of tuples associated with each object
--count_by_object = foreach objects generate flatten($0), COUNT($1) as count PARALLEL 50;
--describe count_by_object;
--count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;
count_by_subject = FOREACH subjects GENERATE flatten($0), COUNT($1) as count PARALLEL 266;
--describe count_by_subject;

--groups_by_count = group count_by_subject by (count) PARALLEL 50;
groups_by_count = GROUP count_by_subject BY (count) PARALLEL 76;
--describe groups_by_count;
--dump groups_by_count;

--final_output = foreach groups_by_count generate flatten($0), COUNT($1) as count PARALLEL 50;
final_output = FOREACH groups_by_count GENERATE flatten($0), COUNT($1) AS count PARALLEL 266;
--describe final_output;
dump final_output;

--order the resulting tuples by their count in descending order
--count_by_object_ordered = order count_by_object by (count)  PARALLEL 50;

--store the results in the folder /user/hadoop/example-results
--store count_by_object_ordered into 'histogram' using PigStorage();
--Alternatively, you can store the results in S3, see instructions:
--store count_by_object_ordered into 's3n://user/example_results.txt';
--store final_output into '/tmp/finaloutput' using PigStorage();

-- Answers: 
-- 1. 1622294 records
-- 2. 2A. 2   (x, y) points
-- 3. 2B. 319 (x, y) points
-- 4. 2998 records
-- 5. 28461 records
-- 6. 3982    (x, y) pointx

