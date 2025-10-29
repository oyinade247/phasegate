import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class WarmUpTest{

	public static void testThatGetNumberOfTheYearWorkAsExpected(){

	WarmUp value = new WarmUp();
	
	double fixedValue = 20000;
	
	double actual = value.getNumberOfYear(fixedValue);
	double expected = 12.0  ;
	assertEquals(actual, expected);






}






}
