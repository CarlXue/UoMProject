import weka.core.Instances;
import weka.core.converters.ArffLoader;
import weka.core.converters.CSVSaver;
import java.io.File;
import java.io.IOException;


public class Arff2CSV {
	public static void main(String[] args) throws IOException {
		//read from Arff format
	    ArffLoader loader = new ArffLoader();
	    loader.setSource(new File("/Users/songxue/Documents/UoMProject/Weather Data/weather-test.arff"));
	    Instances data = loader.getDataSet();
	    //write into CSV format
	    CSVSaver saver = new CSVSaver();
	    saver.setInstances(data);
	    saver.setFile(new File("/Users/songxue/Documents/UoMProject/Weather Data/weather-test.csv"));
	    saver.writeBatch();
	}

}