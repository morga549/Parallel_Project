import java.io.IOException;
import java.util.LinkedList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.List;
import java.lang.Integer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class RedditismKarmaCollector {

    public static class RKCMapper
    extends Mapper<LongWritable, Text, Text, IntWritable>{
        String[] keyWords = {"FTFY", "IMO", "DAE", "ELI5", "IMHO", "TIL", "IIRC", "ITT", "TLDR",
                    "TL;DR","MIC", "MFW", "SMH", "MRW", "AFAIK", "AMA", "FFS", "NFSW", "NSFL",
                    "TIFU", "OP", "/S", "SJW", "NECKBEARD", "KARMAWHORE", "SHITPOST", "CIRCLEJERK"};

        Set<String> redditisms = new HashSet<String>(Arrays.asList(keyWords));

        public void map(LongWritable key, Text value, Context context
        ) throws IOException, InterruptedException {
            List<String> lList = new LinkedList<String>(Arrays.asList(value.toString().toUpperCase().split(" ")));
            int karma = Integer.parseInt(lList.get(0));
            lList.remove(0);
            Set<String> line = new HashSet(lList);

            line.retainAll(redditisms);

            for(String word: line){
                context.write(new Text(word), new IntWritable(karma));
            }
        }
    }

    public static class RKCReducer
    extends Reducer<Text,IntWritable,Text,DoubleWritable> {
        private IntWritable result = new IntWritable();

        public void reduce(Text key, Iterable<IntWritable> values,
        Context context
        ) throws IOException, InterruptedException {
	    double total = 0;
	    int count = 0;
            for(IntWritable value : values){
                total += value.get();
		count++;
            }
	    double output = (double) total / count;
	    context.write(key, new DoubleWritable(output));
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "redditism average karma");
        job.setJarByClass(RedditismKarmaCollector.class);
        job.setMapperClass(RKCMapper.class);
        //job.setCombinerClass(RKCReducer.class);
        job.setReducerClass(RKCReducer.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);
        job.setOutputKeyClass(Text.class);
	job.setOutputValueClass(DoubleWritable.class);
	FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
