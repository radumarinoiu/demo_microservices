package test.microservis;

public class Altceva {
    private double firstNo;
    private double secondNo;
    private double numberSum;

    public Altceva(double firstNo, double secondNo){
        this.firstNo = firstNo;
        this.secondNo = secondNo;
        this.numberSum = firstNo + secondNo;

    }

    public double getFirstNo() {
        return firstNo;
    }

    public double getSecondNo() {
        return secondNo;
    }

    public double getNumberSum() {
        return numberSum;
    }
}
