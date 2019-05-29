package cod_exe;

import org.junit.jupiter.api.Test;

import junit.framework.Assert;

@SuppressWarnings("deprecation")
class test {

	div5ou7 exe = new div5ou7();

	@Test
	void testDivisivel5() {

		String resp = exe.funcDiv5ou7(5);
		Assert.assertEquals("divisível por 5", resp);
	}
	
	@Test
	void testDivisivel7() {

		String resp = exe.funcDiv5ou7(7);
		Assert.assertEquals("divisível por 7", resp);
	}
	
	@Test
	void testDivisivel5e7() {

		String resp = exe.funcDiv5ou7(35);
		Assert.assertEquals("divisível por 5 e 7", resp);
	}
	
	
	@Test
	void testNaoDivisivel5e7() {

		String resp = exe.funcDiv5ou7(13);
		Assert.assertEquals("13", resp);
	}
}
