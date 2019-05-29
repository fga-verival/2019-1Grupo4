package cod_exe;

public class div5ou7 {

	public String funcDiv5ou7(int num){
		
		if(((num%5)==0)&&((num%7)==0)) {
			
			return "divisível por 5 e 7";
		}
		
		if((num%5)==0) {
			
			return "divisível por 5";
		}
		
		if((num%7)==0) {
			
			return "divisível por 7";
		}
		
		return String.valueOf(num);
	}
}
