import weka.core.Instances;
import weka.core.converters.ArffSaver;
import weka.core.converters.CSVLoader;
import java.io.File;

public class CSV2Arff {
	public static void main(String[] args) throws Exception {
      	//read a CSV file
      	CSVLoader loader = new CSVLoader();
      	loader.setSource(new File("/Users/songxue/Documents/UoMProject/Weather Check Project/Numeric Data.csv"));
      	Instances data = loader.getDataSet();
      	//write into Arff format
      	ArffSaver saver = new ArffSaver();
      	saver.setInstances(data);
      	saver.setFile(new File("/Users/songxue/Documents/UoMProject/Weather Check Project/Numeric Data.arff"));
      	saver.writeBatch();
  }

}