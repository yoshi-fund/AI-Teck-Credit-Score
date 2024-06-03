from django.db import models

class Customer(models.Model):
    # 顧客の属性
    outstanding_debt = models.FloatField('債務（ドル建て）') 
    delay_from_due_date = models.FloatField('平均滞納日数')  
    num_of_delayed_payment = models.FloatField('平均滞納回数')
    interest_rate  = models.FloatField('クレカの利息')
    num_bank_accounts = models.FloatField('保有口座数') 
    num_of_loan = models.FloatField('ローンの数') 
    num_credit_card = models.FloatField('クレカの保有枚数') 
    credit_score = models.FloatField(blank=True, null=True)  # 信用スコア（計算後に格納）

    def calculate_credit_score(self):
        # 線形回帰モデルの係数（仮定）
        coefficients = {
            #'intercept': 100,
            'outstanding_debt_coef': -0.236,
            'delay_from_due_date_coef': -0.2,
            'num_of_delayed_payment_coef': -0.16,
            'interest_rate_coef': -0.13,
            'num_bank_accounts_coef': -0.1,
            'num_of_loan_coef': -0.09,
            'num_credit_card_coef': -0.09 
        }
        # 線形回帰式で信用スコアを計算
        self.credit_score = (
            #coefficients['intercept'] +
            coefficients['outstanding_debt_coef'] * self.outstanding_debt +
            coefficients['delay_from_due_date_coef'] * self.delay_from_due_date +
            coefficients['num_of_delayed_payment_coef'] * self.num_of_delayed_payment +
            coefficients['interest_rate_coef'] * self.interest_rate +
            coefficients['num_bank_accounts_coef'] * self.num_bank_accounts +
            coefficients['num_of_loan_coef'] * self.num_of_loan +
            coefficients['num_credit_card_coef'] * self.num_credit_card
        )
        self.save()

    def __str__(self):
        return f"Customer {self.id} - Score: {self.credit_score}"
