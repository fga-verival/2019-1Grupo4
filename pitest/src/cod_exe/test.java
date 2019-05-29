package cod_exe;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import junit.framework.Assert;

@SuppressWarnings("deprecation")
class test {
	
	private div5ou7 exe;

	@BeforeEach
	public void setUp() {
		this.exe = new div5ou7();
	}

	@Test
	void testMaior100() {

		Assert.assertEquals("maior ou igual a 100", exe.funcDiv5ou7(351));

	}
	
	@Test
	void testDivisivel5() {

		Assert.assertEquals("divisível por 5", exe.funcDiv5ou7(5));
		Assert.assertEquals("divisível por 5", exe.funcDiv5ou7(10));
		Assert.assertEquals("divisível por 5", exe.funcDiv5ou7(15));

	}
	
	@Test
	void testDivisivel7() {

		Assert.assertEquals("divisível por 7", exe.funcDiv5ou7(7));
		Assert.assertEquals("divisível por 7", exe.funcDiv5ou7(14));
		Assert.assertEquals("divisível por 7", exe.funcDiv5ou7(21));

	}
	
	@Test
	void testDivisivel5e7() {

		Assert.assertEquals("divisível por 5 e 7", exe.funcDiv5ou7(35));
		Assert.assertEquals("divisível por 5 e 7", exe.funcDiv5ou7(70));

	}
	
	
	@Test
	void testNaoDivisivel5e7() {

		Assert.assertEquals("13", exe.funcDiv5ou7(13));
		Assert.assertEquals("1", exe.funcDiv5ou7(1));
		Assert.assertEquals("3", exe.funcDiv5ou7(3));

	}
}
