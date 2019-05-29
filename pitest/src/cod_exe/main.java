package cod_exe;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class main {

	public static void main(String[] args) throws IOException {
		
		div5ou7 exe = new div5ou7();
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		String input = in.readLine();
		
		int num = Integer.parseInt(input);
		
		System.out.println(exe.funcDiv5ou7(num));
		
	}

}
