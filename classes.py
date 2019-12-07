class pvalue:
    def __init__(self, alpha, pvalue):
        self.alpha = alpha
        self.pvalue = pvalue
    def reject(self, alpha, pvalue):
        if self.alpha > self.pvalue:
            print('Reject the null hypothesis')
        else:
            print('Fail to reject the null hypothesis')
