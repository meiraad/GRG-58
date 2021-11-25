# GRG-58

1. Step function state machine is titled GRG-55, here https://eu-west-2.console.aws.amazon.com/states/home?region=eu-west-2#/statemachines
  Here's its graph: 
  
2. Start execution, using input:
    {
      "SourceBucket": "grg-55-source",
      "SourceObjectKey": "sample.txt",
      "DestinationBucket": "grg-55-dest"
    }
3. In S3, refresh bucket grg-55-dest, the field "Last Modified" should reflect when the step function was last executed. 
4. To view crawler, go to Glue > select crawlers > Glue crawler is named "new-crawler-58".
5. To view Glue table in Athena, in Glue select tables > check off "grg-58-dest" > select action > view data. Data can be queried here.