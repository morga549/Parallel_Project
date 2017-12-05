import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class RedditismKarmaCollector {

    public static class RKCMapper
    extends Mapper<Text, Text, Text, IntWritable>{
        String[] keyWords = ["FTFY", "IMO", "DAE", "ELI5", "IMHO", "TIL", "IIRC", "ITT", "TLDR",
                    "TL;DR","MIC", "MFW", "SMH", "MRW", "AFAIK", "AMA", "FFS", "NFSW", "NSFL",
                    "TIFU", "OP", "/S", "SJW", "NECKBEARD", "KARMAWHORE", "SHITPOST", "CIRCLEJERK"]

        Set<String> redditisms = new HashSet<String>(keyWords);

        public void map(Text key, Text value, Context context
        ) throws IOException, InterruptedException {
            List<String> aList = value.toString().split(" ").asList();
            int lastIdx = aList.size() - 1;
            int karma = Interger.parseInt(aList.get(lastIdx));
            aList.remove(lastIdx);
            Set<String> line = new HashSet(aList);

            line = line.retainAll(redditisms);

            for(String word: line){
                context.write(new Text(word), new IntWritable(karma));
            }
        }
    }

    public static class RKCReducer
    extends Reducer<Text,IntWritable,Text,F> {
        private IntWritable result = new IntWritable();

        public void reduce(Text key, Iterable<IntWritable> values,
        Context context
        ) throws IOException, InterruptedException {
            for(Text value : values){
                context.write(key, value);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "common friends");
        job.setJarByClass(CommonFriends.class);
        job.setMapperClass(CFMapper.class);
        //job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(CFReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
