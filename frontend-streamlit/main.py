import streamlit as st
import requests
import logging
import re

logger = logging.getLogger(st.__name__)
st.set_page_config(
    page_title="Precedent Summariser",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'http://fakeurl.com',
        'Report a bug': "http://fakeurl.com",
        'About': "# Experimental"
    }
)

case = st.text_area("Case", """Press Summary (English)

Press Summary (Chinese)

FACC No. 5 of 2021

[2021] HKCFA 26

IN THE COURT OF FINAL APPEAL OF THE

HONG KONG SPECIAL ADMINISTRATIVE REGION

FINAL APPEAL NO. 5 OF 2021 (CRIMINAL)

(ON APPEAL FROM CACC NO. 131 OF 2018)

________________________

BETWEEN
HKSAR	Respondent
and
LIANG YAOQIANG (梁耀強)	Appellant
________________________

Before:	Chief Justice Cheung, Mr Justice Ribeiro PJ, Mr Justice Fok PJ, Mr Justice Tang NPJ and Mr Justice French NPJ
Date of Hearing:	24 June 2021
Date of Judgment:	21 July 2021
________________________

J U D G M E N T

________________________

Chief Justice Cheung:

1.  Three times between 2010 and 2018, the appellant was tried and convicted after trial of murdering his cohabitee Madam Yeung Sau Yu on 12 September 2009.  On each occasion, the conviction was overturned on appeal – twice by the Court of Appeal[1] and once by this Court[2] (reversing the Court of Appeal’s dismissal of the appellant’s application for leave to appeal[3]) – and a retrial was ordered.  This appeal arose out of the last conviction of the appellant for murder on 26 April 2018.  The conviction was unanimously quashed by the Court of Appeal on 20 November 2020[4].  By a majority decision (Macrae VP and Zervos JA, McWalters JA dissenting), the Court of Appeal ordered a third retrial.  On 29 March 2021, the Appeal Committee gave leave to appeal against the order for retrial[5], and thus this appeal.

The facts

2.  There is no dispute that the appellant killed the deceased on 12 September 2009 in the flat where they cohabited and that he had done so by chopping her with a knife approximately 213 times.  The appellant denied the charge of murder but was prepared to plead guilty to manslaughter by reason of provocation.  At his third trial, a further defence of diminished responsibility, supported by newly obtained psychiatric evidence, was also run.

3.  There was no eye witness to the killing.  Only the appellant and the deceased were present inside the flat at the time.  The defence case on provocation was essentially based on two video records of interview made by the police shortly after the killing, the voluntariness of which was admitted, as well as the appellant’s own evidence at trial.  Essentially, his case on provocation was that the deceased was having an affair with another man (who gave evidence as prosecution witness).  Although the appellant was not sure about it at the time, he had a strong suspicion about the deceased’s infidelity.  Used condoms were on several occasions found by the appellant in the rubbish bin at the rear staircase outside the flat, and on the last time that happened, that is, in the afternoon of 11 September 2009, the appellant confronted the deceased with a used condom which he found in the rubbish bin, which he said was still warm. That led to heated quarrels between the two that same evening and the following morning during which, according to the appellant, the deceased taunted him about becoming a garbage collector, his poor performance as a sexual partner, and that he was not his daughter’s father and she had been fathered by a man who had an affair with his ex‑wife.  According to the deceased’s ex‑husband, the deceased had called him on his mobile at 5:40 am and told him that the appellant had gone crazy, taken off all his clothing and attempted to jump off the building, and she was scared.  According to the appellant, after that telephone call, the deceased twice thrust the used condom into his face near his mouth, asking him to eat it so that he would stop asking her about her new boyfriend.  The appellant claimed that he lost control and his mind went blank.  He fetched a knife from the kitchen, attacked the deceased frenziedly and killed her.  That happened between 6 and 7 am.

The first trial and appeal

4.  The appellant’s first trial took place before Beeson J sitting with a jury in October 2010.  On 21 October 2010, he was convicted of murder by the unanimous verdict of the jury. On 30 October 2013, the Court of Appeal allowed his appeal and quashed the conviction because impermissible hearsay evidence was adduced at trial, with no objection from defence counsel who somehow considered it advantageous to his case.  The Court took the view that given the degree to which the inadmissible evidence went to undermine the defence of provocation, it could hardly be said that the conviction for murder was safe or satisfactory.  The Court of Appeal ordered a retrial.

The second trial and appeals

5.  The retrial took place before V Bokhary J and a jury in March 2014, and again the appellant was convicted of murder by the unanimous verdict of the jury on 31 March 2014.  The sole issue at trial was, as before, whether he had been provoked by the deceased.  He again pleaded guilty to manslaughter on the basis of provocation which was not accepted by the prosecution.

6.  On 30 June 2015, the Court of Appeal, by a majority (Lunn VP and Macrae JA, McWalters JA dissenting on the gravity of the provocation ground), refused leave to appeal against the conviction.  The appellant’s further appeal to this Court was, however, successful.  In its judgment dated 7 February 2017, this Court allowed the appeal and quashed the conviction upon a construction of the phrase “do as he did” in section 4 of the Homicide Ordinance (Cap 339)[6], and held that it had not been dealt with accurately and adequately by the trial judge in her directions to the jury.  This Court ordered a second retrial.

The third trial

7.  The appellant’s third trial before Anthea Pang J and a jury commenced on 8 August 2017.  It was aborted shortly afterwards because of adverse media reporting of the case. Following a series of pre‑trial reviews, in which for the first time the defence indicated its intention to rely on psychiatric evidence to run a new defence of diminished responsibility, the third trial commenced on 10 April 2018 before Maggie Poon J (as she then was) sitting with a jury.  The defence of diminished responsibility, run alongside the original defence of provocation, was supported by a psychiatric report prepared by Dr Wong Chung Kwong who had seen the appellant on 30 June 2017.  The prosecution called Dr Oliver Chan, who had seen the appellant on 2 August 2017 and prepared a psychiatric report dated 22 April 2018, in rebuttal.  According to Dr Wong, the appellant was suffering from an abnormality of the mind arising from the combined effects of two psychiatric disorders, namely a Major Depressive Disorder (“MDD”) of mild to moderate severity, and Acute Dissociative Reactions to Stressful Events (“ADR”) which was a brief, acute and serious disorder, coupled with four underlying factors, namely, hypoglycaemia, sleep deprivation, alcohol and emotional memory of his ex‑wife’s adultery.  Dr Wong took the view that at the time of the killing, the appellant’s abnormality of mind due to these two psychiatric disorders plus the four underlying factors severely compromised his mental capacity to think and judge rationally, and it impaired his ability to control his emotion, impulse and behaviour.  Dr Chan disagreed with Dr Wong’s finding that the appellant had been suffering from MDD at the time of the killing.  Instead he found that he had been suffering from an adjustment disorder.  Dr Chan accepted that the appellant’s discovery of the deceased’s infidelity had been a major life stressor in the two months preceding the killing.  He took the view that an adjustment disorder might be considered as an abnormality of mind, but considered that the appellant’s condition did not substantially impair his mental responsibility for his act, and could not provide a causal explanation for the killing.  However, Dr Chan agreed that the appellant might have been on a highly emotional roller coaster ride just prior to the killing, and that he went into a dissociative state during the attack.

8.  Before counsel’s closing addresses and the judge’s summing up, the judge prepared draft written directions to the jury, setting out the law and issues relating to murder, provocation and diminished responsibility, and invited counsel to comment on them, which counsel did.  In short, the draft directions referred to the psychiatric evidence in the context of diminished responsibility but not provocation.  From the comments made by the appellant’s leading counsel, Mr Andrew Bruce SC, to the judge on the draft directions, it is clear that on the issue of provocation, the only concern leading counsel had was in respect of factual provoking conduct, and the expert evidence on the appellant’s mental health was seen as relevant to the special characteristics of the appellant in considering the “do as he did” element of provocation only.  No mention was made by Mr Bruce of the relevance of the psychiatric evidence to the question of whether the appellant had lost his self‑control.  Mr Philip Chau, counsel for the prosecution, simply expressed his “complete agreement” with Mr Bruce’s comments. In those circumstances, the judge finalised her written directions to the jury on the issues.

9.  In his closing address to the jury, Mr Bruce relied on the psychiatric evidence of Dr Wong in support of his client’s defence of diminished responsibility.  Consistent with his comments on the judge’s draft written directions, when he came to the defence of provocation, the psychiatric evidence was only relied on in relation to the objective question of whether an ordinary sober person would have been provoked given the appellant’s experiences, background, features and attributes relevant to the provocation.  It was not relied on or referred to in relation to the prior, factual question of whether the appellant had or might have lost his self‑control.

10.  The judge’s summing up, in which she directed the jury along the lines of her written directions on the issues, also referred to the psychiatric evidence in the context of the objective question of “do as he did” only, but not the factual question of loss of self‑control.

11.  The jury unanimously returned a guilty verdict of murder and the appellant was sentenced to life imprisonment accordingly.

The appeal below

12.  On appeal, Mr Bruce, for the appellant, successfully ran the argument that the judge misdirected the jury by failing to draw their attention to the psychiatric evidence and its relevance in relation to the issue of whether the appellant lost or might have lost his self‑control[7]. The Court of Appeal unanimously agreed that the psychiatric evidence was “highly relevant”[8] to the factual issue of loss of self‑control, and concluded that the judge’s “clear failure”[9] to direct the jury on the relevance of the psychiatric evidence to this issue resulted in the defence of provocation not being fully and fairly placed before the jury.  The failure “went to the heart of the subjective aspect of the defence”[10], namely whether the appellant lost his self‑control.  The appeal was allowed and the conviction quashed, for the third time, accordingly[11].

13.  What divided the Court in its judgment dated 20 November 2020 was the question of ordering a third retrial, that is, a fourth trial for murder.  Zervos JA, who gave the leading judgment in favour of a third retrial, summarised his reasons for so ordering in paragraph 257 of the judgment:

“ In summary, I am persuaded that the applicant should be retried for a fourth time and my decision includes the following considerations:

(1)  The number of trials and appeals. The applicant has undergone three trials and various appeals and this is a significant factor against ordering a retrial, but this has been outweighed by other factors that have led to the decision that the applicant should be tried for a fourth time. I do not consider that a fourth trial would be oppressive in the circumstances.

(2)  The lapse of time.  The delay in putting the applicant on trial for a fourth time is also a significant factor against ordering a retrial, but bearing in mind the history of the proceedings and nature of the case I do not consider that this will cause any material prejudice to the applicant.

(3)  The need for finality.  This is an important consideration that must also be considered together with the seriousness of the offence.  It is desirable that the guilt or innocence of the applicant for the alleged offence of murder be finally determined by a jury. This consideration not only takes into account the interests of the applicant, but also the interests of the victim’s family and the interests of the public.

(4)  The seriousness of the offence and the strength of the case.  This case involves an alleged offence of murder.  There is no question that the applicant killed the deceased.  The issue at trial is whether the applicant killed the deceased with murderous intent or whether he was provoked or suffering from diminished responsibility at the time of the killing.

(5)  The length and complexity of a fourth trial.  This is a fairly straightforward case where the issues are well defined.

(6)  The nature of the case and the matters in issue.  The questions to be addressed in evaluating the defences are preeminently ones for a jury and it is clearly preferable for a jury to determine if the applicant’s conviction for killing the deceased should be for murder or the lesser crime of manslaughter.

(7)  The alternative conviction of manslaughter.  A serious crime of murder is alleged against the applicant and it is in the interests of the public that persons charged with such serious crime have the charge determined by a court of law, and if found guilty, are appropriately punished.

(8)  The length of time served.  The applicant if convicted of murder would be sentenced to life imprisonment.

(9)  Whether the applicant can receive a fair trial.  It is said that there will be difficulties in the applicant receiving a fair trial because of (i) his previous statements and evidence; and (ii) media publicity of the case.  If an issue should arise in relation to these matters they can be appropriately dealt with in the trial process.

(10)  The history of the proceedings and the applicant’s responsibility for the mistrials and delay.  It would seem that the applicant is partly responsible for the delay in the proceedings because of the way he has run the defence case which at the third trial changed to include the defence of diminished responsibility.  There is also the factor that the applicant’s conviction has been quashed because of a misdirection by the judge for which leading counsel was partly responsible.

(11)  The applicant’s mental condition.  It does not appear that the applicant’s mental condition would preclude ordering a retrial either on that basis or together with other factors, namely undergoing a fourth trial and the lapse of time since the offence took place.”

14.  Earlier in his judgment, Zervos JA had said that this was a case where “the circumstances which brought about the possibility of a retrial were, in no small measure, due to the conduct of the [appellant] or those acting for him”[12]. The judge was critical of Mr Bruce’s failure to point out to the trial judge the relevance of the psychiatric evidence to the factual question of whether the appellant had or might have lost his self‑control under the provocation defence[13]. He referred to it as a possible “tactical decision” on the part of leading counsel[14]. In paragraph 212 of the judgment, Zervos JA commented:

“ It is clearly apparent from the highlighted comments of Mr Bruce in his closing address that he made no mention of the psychiatric evidence under the first limb of provocation, and only specifically discussed the psychiatric evidence under the second limb. This approach by the defence gives the impression that a tactical decision may have been made to lay emphasis on the alleged provocative conduct of the deceased, ensuring the impact of it was not lessened by reference to the psychiatric evidence, in order to establish that the applicant was or might have been provoked.”

15.  In his short concurring judgment, Macrae VP gave five reasons for favouring another retrial: first, this was a case of murder, the most serious offence in the criminal calendar.  It was important from everyone’s point of view, not least the family of the deceased, that there be a proper adjudication, according to law, of the guilt of the accused in respect of such a serious offence[15]. Secondly, there was no issue as to whether the appellant killed the deceased. The issues arising from the appellant’s two defences would best be resolved by a jury which hears the evidence rather than by an appellate court which reads it[16]. Thirdly, given the nature of the appellant’s defences, the issue would necessarily turn on what was in the mind of the appellant at the time he killed the deceased.  The appellant’s own recollection was likely to be vivid and graphic, and thus the lapse of time and its effect on the appellant’s memory was more apparent than real as a problem.  Appropriate directions could also be given at the retrial to make allowances for the fact that with the passage of time memories fade[17]. Fourthly, the third trial was the first trial at which the appellant had advanced the issue of diminished responsibility[18]. Fifthly, the judge’s error was contributed to by the submissions of the appellant’s leading counsel himself[19].

16.  Disagreeing with the majority, McWalters JA took the view that enough was enough.  In paragraph 143 of the Court of Appeal’s judgment, he summarised the factors which persuaded him to come to that conclusion:

“ I am persuaded into adopting this course by the following factors:

(i)  on the assumption that the applicant was awarded a discount of one third for his offer to plead guilty to manslaughter[20] then the applicant has, in effect, already served a fixed term sentence of approximately 23 years’ imprisonment[21];

(ii)  the applicant has been forced to undergo the ordeal of three trials and multiple appeals over the course of 11 years and as a consequence a fourth trial to determine whether he is guilty of murder, as opposed to manslaughter, would be oppressive to him;

(iii)  there would be considerable difficulties in ensuring that a fourth trial would be a fair trial;

(iv)  a substituted verdict means that the applicant does not escape justice and does not go unpunished for his crime;

(v)  a substituted verdict will bring finality to the proceedings arising from this crime and this will provide additional benefits of:

(a)  a saving to the public purse; and

(b)  closure for the applicant and his family; and

(vi)  on a properly conducted retrial a verdict of manslaughter cannot be said to be an unlikely verdict as there was independent evidence of provocative conduct by the deceased and the murderwas clearly committed in a frenzied state consistent with a loss of self‑control. I note that in R v Bell the English Court of Appeal said of a third trial for murder:

‘The broad public interest in the administration of criminal justice leads us to the clear view that a second re‑trial should be confined to the very small number of cases in which the jury is being invited to address a crime of extreme gravity which has undoubtedly occurred (as here) and in which the evidence that the defendant committed the crime (again, as here) on any fair minded objective judgment remains very powerful.’[22]

I am not persuaded that it can be said that on a fair minded objective judgment, the evidence ‘remains very powerful’ for the return of a verdict of murder, as opposed to a verdict of manslaughter.”[23]

17.  As for the suggested “tactical decision” of Mr Bruce which contributed to the trial judge’s error in her directions to the jury, McWalters JA had this to say:

“ In respect of the conduct of Mr Bruce, Zervos JA is particularly concerned that it may reflect a deliberate tactical choice by him in the conduct of the defence case. I am not persuaded that the transcript supports such a conclusion. I cannot see in this case, in contrast with what occurred in the first trial, any positive action by Mr Bruce or Mr Chau to persuade the Judge to pursue a particular course and nothing was said or done by either counsel to mislead the Judge. I cannot see any basis for suggesting that Mr Bruce intentionally stood by and allowed the Judge to fall into error. Nor can I see how any tactical benefit would accrue to the applicant by not reminding the jury of the relevance of the psychiatric evidence to their decision on the issue of loss of control. Indeed, quite the contrary. It was positively adverse to the applicant and that is why we are allowing the appeal. I cannot, therefore, agree that there is a basis for concluding that Mr Bruce deliberately pursued a tactical course in his conduct of the defence case which contributed to the error of the judge which lead to this appeal being allowed.”[24]

Leave to appeal

18.  On 29 March 2021, the Appeal Committee (Ribeiro PJ, Fok PJ and Tang NPJ) granted leave to appeal on the substantial and grave injustice basis on the footing that it was reasonably arguable that in ordering a third retrial for murder, the exercise of discretion by the majority of the Court of Appeal miscarried.

The arguments before us

19.  Before us, Mr Robert Pang SC (Ms Denise Souza with him), for the appellant, relied on three grounds[25]. First, the majority of the Court of Appeal wrongly took into account the conduct of the appellant’s legal representatives in his previous trials, particularly the third trial, as factors which were relevant and justified a further retrial.  In particular, counsel argued that although Mr Bruce did comment on the judge’s draft written directions and failed to point out the relevance of the psychiatric evidence to the factual question of losing self‑control under the defence of provocation, that was a mistake shared by prosecuting counsel as well as the judge herself.  It was not the result of any “tactical decision” on the part of Mr Bruce and it was an irrelevant consideration.  No tactical advantage was ever identified by the majority.  As for the raising of the defence of diminished responsibility and the reliance on psychiatric evidence only for the first time at the third trial, Mr Pang submitted that it was a viable defence and the appellant was entitled to raise it.  The new defence did not cause any delay or adjournment.  There was no suggestion that the psychiatric evidence was unnecessary or was time wasting.

20.  Secondly, counsel argued that the majority did not sufficiently consider whether the prosecution had a strong case for murder.  The fact that the killing was admitted did not mean that the prosecution had a strong case.  The issue was whether the prosecution had a strong case that the appellant was not legally provoked into killing the deceased.  In light of the evidence of the appellant, the circumstances and the psychiatric evidence, counsel submitted that the strength of the prosecution’s case was not as strong as the majority thought it to be.

21.  Thirdly, counsel submitted that the majority failed to sufficiently consider whether the delay or lapse of time in proceedings rendered an order for retrial oppressive and unjust, or a breach of the appellant’s right to be tried without undue delay under article 11(2)(c) of the Hong Kong Bill of Rights[26]. Counsel submitted that the majority failed to realise that the right to be tried without undue delay is a separate or independent right from the right to a fair trial[27] and the order for a third retrial breached the appellant’s right.

22.  Counsel asked the Court to substitute the conviction for murder with a conviction for manslaughter on the basis of provocation, and sentence the appellant accordingly.

23.  For the respondent, Mr William Tam SC (Mr Ira Lui and Mr Andy Lo with him) pointed out that a fourth trial for murder is not unprecedented[28]. The law has given the discretion to order a retrial to the Court of Appeal, rather than to this Court.  This Court should, therefore, not lightly disturb the exercise of discretion by the Court of Appeal.  The Court of Appeal was in disagreement only on the weight to be attached to certain factors and ultimately favoured a retrial by a majority.  The majority and the minority each had the benefit of considering and debating the detailed reasons of the other side.  There was no cogent reason for suggesting that the majority had erred in principle or had taken into account irrelevant factors.  Whilst the issue might be finely balanced, there was no reason to interfere with the exercise of discretion by the majority, even if this Court might “lean in favour of an exercise of it the other way”[29].

24.  As for the conduct of the appellant’s counsel at the third trial, Mr Tam emphasised that the jurisdiction to order a retrial is put in the widest possible terms.  As a matter of principle, there is no justification for excluding from the Court of Appeal’s consideration the conduct of an accused’s legal representatives.

25.  Counsel also submitted that the majority’s focus, when referring to the appellant’s counsel’s conduct at the third trial, was on the cause and consequence of the technical blunder by the trial judge.  The majority’s emphasis was on the nature of the error and not on an attribution of fault.  In any event, the majority only considered that counsel’s contributing fault was a material matter to be taken into account.  It did not treat it as a determinative one[30].

26.  Counsel accepted that the majority of the Court of Appeal did not elaborate on why the raising of diminished responsibility as a partial defence at the third trial only was relevant to the question of retrial.  He suggested that if the defence had been raised earlier, the relevance of the psychiatric evidence could have been sorted out either at trial or on appeal on an earlier occasion.

27.  As for the strength of the prosecution case, Mr Tam pointed out that the appellant’s defence turned entirely on his own evidence and the psychiatric evidence.  He submitted that the appellant’s testimony was self‑contradictory, unreasonable and inconsistent with the account in his video interviews.  In relation to expert evidence, Dr Oliver Chan’s evidence in rebuttal was obviously preferred by the jury.  Counsel also pointed out that the appellant had been disbelieved unanimously in all his previous trials.  The defence of diminished responsibility was plainly rejected by the jury.  Whether the appellant was or might have been provoked into killing the deceased was eminently a task for the jury.

28.  As regards the question of delay and fair trial, Mr Tam pointed out that a fair trial is a trial fair to all parties, and not only to the accused.  He emphasised that murder is one of the most serious crimes and the public interest in seeing that the murder charge against the appellant for the brutal killing of the deceased was resolved by a jury at trial was very strong.  It was submitted that the issues involved in the retrial would be within a very narrow compass and the retrial was unlikely to be lengthy.  There was no suggestion of the appellant having difficulties in recalling the events due to the lapse of time, and indeed he had no difficulties in giving a very detailed account to the psychiatrists when they interviewed him over eight years after the killing.  In any event, any difficulties would be mitigated by reference to the appellant’s police interviews and transcripts of his evidence in the earlier trials.  Moreover, the trial judge could, if required, give the jury appropriate directions.  A lapse of time of some twelve years would not in itself forbid a further retrial.

29.  Mr Tam also argued that a lapse of time amounting to a breach of the right to a fair trial within a reasonable time does not per se render an otherwise fair trial and a resulting conviction unlawful.  A breach of the reasonable time requirement would only entitle the convicted person to remedies such as a reduction in penalty and payment of compensation[31].

The legal principles

30.  The power to order a retrial is found in section 83E(1) of the Criminal Procedure Ordinance (Cap 221).  It provides:

“Where the Court of Appeal allows an appeal against conviction and it appears to the Court of Appeal that the interests of justice so require, it may order the appellant to be retried.”

31.  The principles governing the exercise of this statutory discretion to order a retrial are well established.  They were revisited by this Court as recently as last year in HKSAR v Zhou Limei (No 2)[32], and it is quite unnecessary to go into the earlier authorities again.  In paragraph 9 of this Court’s judgment, Chief Justice Ma, giving the leading judgment of the Court, reiterated a number of relevant principles from the decided cases on retrial:

“ Section 83E of the Criminal Procedure Ordinance states that the Court of Appeal, if it decides to allow an appeal, may order a retrial if ‘the interests of justice’ so require. The jurisdiction to order a retrial is thus put in the widest possible terms. In HKSAR v Tam Ho Nam (No 2),[33]Fok PJ restated the relevant principles regarding retrials by reference to Au Pui Kuen v Attorney General of Hong Kong,[34]Ting James Henry v HKSAR[35]and Kissel v HKSAR.[36] The following principles, distilled from the above and other cases, are relevant in the present case:

(1)   Whether or not a retrial should be ordered is a matter of discretion. This discretion is usually exercised, as it should be, by the Court of Appeal, relying on their ‘collective sense of justice and common sense.’[37] And, as was put by Lord Bingham of Cornhill, there must be ‘an informed and dispassionate assessment of how the interests of justice in the widest sense are best served’; it is important to maintain ‘confidence in the efficacy of the criminal justice system.’[38]

(2)   The discretion whether or not to order a retrial depends entirely on what justice requires (this being the ‘critical question’).[39]

(3)   The interests of justice of course include a consideration of an accused’s interests and circumstances. The criminal justice system is there to bring matters to a conclusion without undue delay and without oppression; these are ‘accepted norms’.[40] It should be acknowledged that any criminal trial is to some degree an ordeal for the accused.[41] The interests of justice also include the interest of the public in seeing those who are guilty of serious crimes brought to justice and not escape merely because of a technical error in the conduct of a trial or in the summing up to a jury.[42] In Au Pui Kuen v Attorney General of Hong Kong,[43]Lord Diplock referred to the following passage from the judgment of Gould Ag CJ in Ng Yuk Kin v The Crown:[44]that there may be cases where it ‘is in the interest of the public, the complainant, and the appellant himself that the question of guilt or otherwise be determined finally by the verdict of a jury, and not left as something which must remain undecided by reason of a defect in legal machinery’. In assessing the public interest, a court must take into account the views of the prosecution which is best qualified (and I would add has the duty) to present the views of the public,[45]although it must ultimately be for the court to determine what is in the public interest. The strength of the prosecution case is also a relevant consideration.

(4)   The interests of justice require all relevant factors, both for and against a retrial, to be taken into account. Such factors will not only vary from case to case, but their relative importance and weight will also be different in any given case.[46]

(5)   The above said, one factor that must be given significant weight is the fact that the accused has already undergone a trial, in particular where the trial is long and complex.[47] This is all the more so when there is involved a second retrial, which means of course the possibility of a third trial for the same offence. In Mok Kin Kau v HKSAR,[48]the ordering of a second retrial after two concluded trials and appeals, and the serving of the whole sentence, was said to be an ‘unusual course’ and in such a situation, in the absence of a special or compelling reason, this was a ‘departure from accepted norms’ sufficient to constitute a substantial and grave injustice. Although it is not unprecedented for a second retrial to be ordered, the cases accept that this is an ‘unusual’ course to take,[49]even where the accused has not served the whole of his or her sentence as was the case in Mok Kin Kau v HKSAR. Given that the ordering of a second retrial is an unusual course, a court would have to be persuaded by cogent and compelling reasons to make such an order. This is consistent with the interests of justice, but of course all relevant factors must be carefully weighed in this exercise of discretion.

(6)   Another factor that should also be taken into account is the time that an accused has spent in custody and in relation to this facet, the time that an accused has been in custody will have to be seen against the likely sentence that he or she might receive on a retrial.[50]”[51]

32.  The printed cases of the parties referred to a number of cases in which the courts considered how the discretion to order a retrial should be exercised[52]. Of course, each case turns on its own facts.  The reference to how the discretion to order a retrial was exercised in a previous case, even of broadly similar facts, is bound to be of limited assistance.

33.  As already mentioned, the primary responsibility for exercising the discretion to order a retrial lies with the Court of Appeal, after quashing a conviction below.  As explained in Zhou Limei (No 2)[53], this Court would only intervene in limited circumstances:

“ In common with the review of discretion in other areas, this Court will not disturb the exercise of discretion by the Court of Appeal in the determination whether or not to order a retrial unless there has been a serious error of law or principle or approach, such as where the court below has failed to take into account a relevant consideration or has taken into account an irrelevant one. Only in such a situation would the Court of Final Appeal be justified in exercising the discretion afresh. Furthermore, it is also important to emphasise that the relative weight which the Court of Appeal ‘ascribes to each relevant factor’ is a matter within its discretion and it is not open to the Court of Final Appeal to seek to ascribe a different weight.[54]”[55]

The majority’s exercise of discretion

34.  Turning to the facts of the present case, a major difference between the majority and the minority on the question of retrial was whether Mr Bruce (and, vicariously, the appellant himself) contributed to[56] or was “partly responsible”[57] for the error made by the judge in her directions on the issue of loss of self‑control insofar as the relevance of the psychiatric evidence was concerned.  Although couched in cautious terms, it is plain from a fair reading of the judgments of Macrae VP and Zervos JA that they considered defence counsel was deliberate in not drawing to the judge’s attention the relevance of the psychiatric evidence to the question of loss of self‑control.  Instead, he simply stood by and allowed her to fall into error, for the purpose of achieving a tactical benefit.  That certainly was how McWalters JA understood their position[58].  He gave his reasons for disagreeing with the view of the majority on the role played by defence counsel in the judge’s mistake.  I find his reasons persuasive.

35.  No doubt, the judge was in error when she overlooked entirely the relevance of the psychiatric evidence to the question of provocation in her initial draft directions which she showed to counsel for comments.  It is also true that Mr Bruce only referred to the psychiatric evidence in relation to the objective question of “do as he did” under the defence of provocation.  He made no mention of the relevance of the expert evidence to the question of loss of self‑control. The same omission was repeated in his closing address.  To that extent, Mr Bruce, like prosecuting counsel, may properly be regarded as having played a part in the judge’s mistake in overlooking the relevance of the expert evidence to the question of loss of self‑control.

36.  However, the majority obviously went much further.  They thought that defence counsel must have also been aware of the relevance of the expert evidence to the question of loss of self‑control but by a deliberate, tactical decision he chose to keep quiet about it and let the judge err.  According to Zervos JA, this was to achieve a tactical advantage which he explained in paragraph 212 of his judgment.  If the learned judge were right on his view, this would have been a very serious matter, contributing substantially to the trial judge’s omission in her directions and thus the eventual quashing of the jury’s verdict, and it would have been right to take it critically against the appellant on the question of retrial.  And indeed quite apparently, that was Zervos JA’s approach although he was careful to say that this was not by itself determinative of the question of retrial[59].

37.  With respect, I am unable to subscribe to Zervos JA’s view.  First, it was the trial judge who first overlooked the relevance of the expert evidence to the question of provocation altogether in her initial draft directions.  There is no suggestion that Mr Bruce played any part in it.  According to the transcript, after reading the initial draft directions, Mr Bruce recognised the relevance of the expert evidence to the objective question of “do as he did” and made his comments to the judge accordingly.  Significantly, after he had done so, neither the judge nor prosecuting counsel who agreed with Mr Bruce on the relevance of the evidence to the objective question realised that the expert evidence was also material to the earlier question of loss of self‑control.  In terms of failing to appreciate the relevance of the expert evidence to that question, all three of them – the judge, prosecuting counsel and defence counsel – were on an equal footing.  Judging from the transcript[60], there was really nothing to differentiate them from one another in this regard, and there was certainly nothing to justify singling Mr Bruce out by suggesting that his failure to point out the relevance of the expert evidence to the question of loss of self‑control was a deliberate, tactical one, whereas the same failure of the judge and prosecuting counsel was a mere error on their part. It is true that at the hearing before the Court of Appeal, when asked about it, Mr Bruce could not give a satisfactory answer for his not spotting the relevance of the expert evidence to the question of loss of self‑control at the time of trial[61]. But there could be many reasons for this, and in the absence of convincing evidence, I am not prepared to draw any adverse inference against leading counsel.

38.  This brings me to the so‑called “tactical benefit” that Mr Bruce was supposed to be seeking to obtain for his client.  Zervos JA sought to articulate it in paragraph 212 of his judgment.  However, with respect, I share McWalters JA’s inability to comprehend the supposed tactical advantage that defence counsel was seeking to achieve[62]. The psychiatric evidence was supportive of the appellant’s case on provocation not only on the objective question of “do as he did”, but also on the factual question of loss of self‑control.  It is difficult to see how any tactical benefit would be achieved for the appellant by not pointing that out to the judge and to the jury.  Any suggestion that defence counsel was seeking to lay the foundation for a ground of appeal would not make any sense at all unless the conviction of the appellant for murder by the jury was a foregone conclusion.  However, I do not see any material to suggest that.

39.  In any event, whether the fault of defence counsel should be attributed to the defendant must depend on the facts of each case.  Even if Mr Bruce were really guilty of deliberately withholding the relevance of the psychiatric evidence to the question of loss of self‑control from the judge (and the jury), the extent to which the appellant should be held vicariously responsible for it would still be highly debatable, particularly when there was nothing to suggest that the appellant was a party to whatever tactical decision that leading counsel might have made on his behalf.

40.  Both Macrae VP and Zervos JA thought the fact that diminished responsibility was only raised for the first time at the third trial was a matter that should be counted against the appellant[63]. With respect, I disagree.  There is no suggestion that diminished responsibility was not an arguable defence in the present case.  After all, it was supported by expert evidence.  It was available to the appellant, and he was entitled to run it.  The running of that defence at the third trial did not cause any significant delay in the proceedings.  The fact that the running of that defence entailed the introduction of the psychiatric evidence at the trial which, as it happened, played a crucial part in the error committed by the judge in her summing up was neither here nor there.  Zervos JA thought that the raising of this additional defence at the third trial “was partly responsible for complicating the defence of provocation”[64]. I cannot see this as a valid criticism against the appellant on the question of retrial, nor do I see this as a reason for visiting the judge’s error upon the appellant for running an additional defence at the third trial.

41.  Mr Tam’s suggestion that had the partial defence been first raised at the first or second trial, the relevance of the psychiatric evidence to the question of loss of self‑control could have been sorted out earlier is speculative at best.  In any event, it is difficult to see how and why the appellant should be held responsible for its late raising by his legal representatives given the highly technical nature of the defence.

42.  For these reasons, I take the view that the majority of the Court of Appeal has misapprehended what happened at the trial and taken into account irrelevant considerations when exercising the discretion to order a third retrial.  The exercise of discretion miscarried, and it falls to this Court to re‑exercise it. This is one of those rare cases where it is justified for this Court to interfere with the exercise of discretion on retrial by the Court of Appeal.

Re‑exercising the discretion

43.  Section 83E(1) of the Criminal Procedure Ordinance provides that the Court of Appeal may order a retrial “if it appears to the Court of Appeal that the interests of justice so require”.  Exercising afresh the discretion conferred on the Court of Appeal, I cannot be satisfied that the interests of justice require a further retrial.  Indeed I am satisfied that they do not.

44.  The relevant considerations that should be taken into account have been discussed in quite some detail by McWalters JA in his dissenting judgment[65], and they have been summarised in paragraph 143 of his judgment which I have already quoted.  Leaving aside the supposed fault and responsibility of defence counsel at trial and the fact that diminished responsibility was only relied on for the first time at the third trial, the other considerations mentioned by Zervos JA in his judgment[66] are also relevant ones and I bear them in mind as well.

45.  Amongst these relevant considerations, I would emphasise the following matters which, when considered together, decidedly tilt the balance against ordering a third retrial.  First, if such an order were made, this would be the fourth full trial for murder that the appellant would be forced to face.  At the retrial, he would have to undergo the substantial forensic challenge of recalling the parties’ relationship and the details of the killing at trial, and be subjected to cross‑examination on them.  He would also have to face the stress and anxiety over the uncertainty of the outcome of the retrial.  These would only be some of the matters that the appellant would have to endure in a fourth trial.  As has been observed[67], any criminal trial is “to some degree an ordeal for the accused” and “it goes without saying that no judge exercising his discretion judicially would require a person who had undergone this ordeal once to endure it for a second time unless the interests of justice required it”.  McWalters JA was obviously correct when he pointed out that “[t]he more often the defendant has to face trial, the greater the ordeal will be for him, and the less fair the criminal justice process will be perceived to be”[68]. In the present case, the appellant has already undergone three full trials, three appeals in the Court of Appeal, as well as two appeals in this Court over the last eleven years, which is, on any view, a very lengthy period of time. There must come a point at which the question – what do the interests of justice require? – is answered by saying “enough is enough”, and to order another retrial would simply be oppressive to the defendant.

46.  Secondly, the appellant has already been remanded in custody for almost twelve years. That is equivalent to a starting point of almost 27 years’ imprisonment assuming a conviction for manslaughter, given the conventional one‑third discount for his early plea of guilty, as well as another one‑third remission by the Commissioner of Correctional Services for good behaviour (as to which there is no dispute)[69]. It is true that if the appellant were to undergo a fourth trial and be found guilty of murder, he would be sentenced to imprisonment for life, and this would mean, very generally speaking, anything between 20 to 30 years’ imprisonment before he might be paroled.  Yet it has to be remembered that if upon retrial, he were only found guilty of manslaughter, a starting point of almost 27 years’ imprisonment would be way beyond the higher end of the usual range of sentences for manslaughter, even after taking into account the horrendous manner in which the killing was committed[70].

47.  Thirdly, I fully bear in mind that the appellant is charged with murder, one of the most serious crimes in our statute books, and this is a particularly brutal case. The public interest in seeing that the murder charge is resolved by a jury after trial is extremely great, not to mention the interest of the deceased’s family in seeing that justice is done.  I also bear in mind that the issues involved in the case are relatively straightforward and narrow, and the trial is not likely to be lengthy.  I give due weight to the view of the prosecution as representing the public interest that although this case is testing the limits of the discretion to order a retrial, the public interest inclines in favour of a fourth trial.  However, after the lapse of almost twelve years, the memory of the appellant as well as that of the witnesses of the relevant events must have been affected to some extent, and there is a difference between giving evidence on the basis of one’s recollection and impression at the time and reconstructing one’s memory and perception from witness statements and transcripts.  The quality of the evidence as well as the demeanour of the witnesses are bound to be affected.  Given that the issues in a fourth trial would turn very much on the performance of the appellant in the witness box, I would be slow to say that any prejudice that he might suffer at the trial could be satisfactorily remedied by appropriate directions to the jury.  On the other hand, unlike those cases where the choice faced by the court was either to order a retrial or to let the accused go free without any conviction, not ordering another retrial here would not mean the appellant could leave as an innocent man.  He would still be convicted and sentenced for manslaughter.

48.  This brings me to the fourth matter, namely, the strength of the prosecution case for murder.  The issue here is a narrow one, as the killing of the deceased by the appellant has been admitted from day one.  The contest is between murder and manslaughter (by reason of provocation or diminished responsibility).  It is true that the appellant has been convicted for murder three times by three juries.  However, the trial process on each occasion was flawed.  On the facts and evidence before us, I would say that the defence of provocation, which is supported by the appellant’s story (which to some extent is corroborated by the deceased’s former husband’s evidence), the circumstances under which the killing took place and the psychiatric evidence, is at least reasonably arguable and a murder verdict is certainly not a foregone conclusion.

49.  Fifthly, the quashing of the convictions in the first and third trials was in part due to mistakes contributed to by defence counsel then representing the appellant. However, for the mistake in the first trial, as McWalters JA explained[71], the primary responsibility lay with the prosecutor.  As for the mistake in the third trial, for the reasons given above, it was not the result of any deliberate, tactical decision on the part of defence counsel, still less that of the appellant.  In my view, they carry little if any weight when considering how the discretion should be exercised.

50.  Looking at the matter in the round, I have come to the conclusion that the discretion should be exercised against ordering a retrial.  Regrettably, the reality in the present case is that the criminal justice system, despite three attempts, has failed not only the deceased’s family and the public, but also the appellant.  I think we have reached a point where enough is enough, and the interests of justice are no longer served by continuing with the prosecution of the appellant for murder.  Rather, a conviction for manslaughter on the basis of provocation should be entered on the appellant’s plea of guilty and the appellant sentenced accordingly, thereby bringing finality and closure to this tragic case.

Sentence

51.  Generally speaking, it is not the function of this Court to pass sentences in criminal cases.  That is the function of the trial court and, on appeal, the Court of Appeal.  However, on the wholly exceptional circumstances of this case, it is right for this Court to sentence the appellant for manslaughter.  As mentioned, the appellant has been in custody for almost twelve years which will be counted as service of his sentence.  Mr Tam, Deputy Director of Public Prosecutions, very fairly accepted that bearing in mind the one‑third discount for the early plea of guilty and the one‑third remission for good behaviour by the Commissioner of Correctional Services, the time that the appellant had spent in custody would have exceeded whatever sentence that this Court might legitimately pass in the present case on the basis of a manslaughter conviction. Mr Tam agreed that amongst the authorities for sentencing placed before the Court[72], the highest sentence imposed was 16 years[73], which is of course far less than the starting point of almost 27 years that the time the appellant has already spent in custody would represent.

52.  In the circumstances, I would quash the order for a third retrial, enter a conviction for manslaughter on the basis of provocation and sentence the appellant to such sentence that would allow for his immediate release from custody.

Mr Justice Ribeiro PJ:

53.  I agree with the judgment of the Chief Justice.

Mr Justice Fok PJ:

54.  I agree with the judgment of the Chief Justice.

Mr Justice Tang NPJ:

55.  I also agree.

Mr Justice French NPJ:

56.  I agree with the orders proposed by the Chief Justice and his reasons for them.

Chief Justice Cheung:

57.  Accordingly, the court unanimously allows the appeal and makes the orders set out in paragraph 52 above.


(Andrew Cheung)	(R A V Ribeiro)	(Joseph Fok)
Chief Justice	Permanent Judge	Permanent Judge


(Robert Tang)	(Robert French)
Non-Permanent Judge	Non-Permanent Judge
                    
Mr Robert Pang SC and Ms Denise Souza, instructed by Tse Yuen Ting Wong, assigned by the Director of Legal Aid, for the appellant

Mr William Tam SC, DDPP, Mr Ira Lui, ADPP and Mr Andy Lo, SPP, of the Department of Justice, for the respondent

""")
reference = st.text_area("References", """ 
[1] [2014] 4 HKC 145 and [2021] 1 HKLRD 26 (“CA judgment”).

[2] (2017) 20 HKCFAR 1.

[3] [2015] 5 HKLRD 743.

[4] [2021] 1 HKLRD 26.

[5] [2021] HKCFA 12.

[6] Section 4 reads: “Where on a charge of murder there is evidence on which the jury can find that the person charged was provoked (whether by things done or by things said or by both together) to lose his self‑control, the question whether the provocation was enough to make a reasonable man do as he did shall be left to be determined by the jury; and in determining that question the jury shall take into account everything both done and said according to the effect which, in their opinion, it would have on a reasonable man.”

[7] CA judgment, [62].

[8] Ibid, [84].

[9] Ibid, [84].

[10] Ibid, [90].

[11] Ibid, [259].

[12] Ibid, [226].

[13] Ibid, [205]-[214], [226], [251].

[14] Ibid, [146], [212].

[15] Ibid, [3].

[16] Ibid, [4].

[17] Ibid, [5].

[18] Ibid, [6].

[19] Ibid, [7].

[20] In my view, as a matter of legal principle, the applicant should be accorded a full one‑third discount on the sentence as he has all times offered to plead guilty to manslaughter and in none of his trials has he ever sought a complete acquittal.  On arraignment, he pleaded guilty to manslaughter.

[21] 23 years discounted by one third is 15 years 4 months which when discounted again by one third to allow for remission by the Commissioner for Correctional Services is 10 years 2 months.

[22] [2010] 1 Cr App R 27, 418, [46].

[23] Original footnotes included.

[24] CA judgment, [124].

[25] At the oral hearing, counsel’s submissions focused on the first ground only.

[26] The Hong Kong Bill of Rights Ordinance (Cap 383), section 8.

[27] Hong Kong Bill of Rights, article 10.

[28] R v Davis (Iain Lawrence) [2011] EWCA Crim 2156; Andrew John Hawkins (No 3) (1994) 76 A Crim R 47; Shane Michael Martin (No 4) (1999) 105 A Crim R 390.

[29] HKSAR v Chu Chi Wah FAMC 58/2010, 2 November 2010, [3].

[30] CA judgment, [252].

[31] Attorney General’s Reference (No 2 of 2001) [2004] 2 AC 72; Henworth v The United Kingdom (2005) 40 EHRR 33; Vlad v Romania (2014) 59 EHRR 13.


[32] (2020) 23 HKCFAR 169.

[33] (2017) 20 HKCFAR 414.

[34] [1980] AC 351.

[35] (2007) 10 HKCFAR 632.

[36] (2010) 13 HKCFAR 27.

[37] Au Pui Kuen v Attorney General of Hong Kong [1980] AC 351, 357D–E.

[38] B (a Child) v R [2001] UKPC 19, [39].

[39] HKSAR v Tam Ho Nam (No 2) (2017) 20 HKCFAR 414, [21].

[40] Mok Kin Kau v HKSAR (2008) 11 HKCFAR 1, [10].

[41] Au Pui Kuen v Attorney General of Hong Kong, 356H.

[42] Au Pui Kuen v Attorney General of Hong Kong, 357C–D.

[43] At 359D–E.  See also Reid (Dennis) v R [1980] AC 343, 350G–H.

[44] (1955) 39 HKLR 49, 60.

[45] Ting James Henry v HKSAR, [51].

[46] Au Pui Kuen v Attorney General of Hong Kong, 357D–E.

[47] Ting James Henry v HKSAR, [50].

[48] At [12] and [14].

[49] See HKSAR v Tam Ho Nam (No 2), [24] referring to R v Chau Mei Ling [1981] HKC 542, 545B–C; Mok Kin Kau v HKSAR, [7]; HKSAR v Li Yanhong (No 2) [2016] 1 HKLRD 946, [14].

[50] See, for example, Ting James Henry v HKSAR, [52].

[51] Original footnotes included (with some omissions).

[52] Ting Henry James v HKSAR; HKSAR v Tam Ho Nam (No 2); HKSAR v Zhou Limei (No 2); Au Pui Kuen v Attorney General; Mok Kin Kau v HKSAR; Reid v The Queen; Charles and Ors. v The State [2000] 1 WLR 384 (PC); Henworth v United Kingdom; Vlad v Romania; R v Lazarus [2017] NSWCCA 279; HKSAR v Lee Ming Tee HCCC 191/1999, 8 June 2004; HKSAR v Li Yanhong (No 2); Nguyen Anh Nga v HKSAR (2017) 20 HKCFAR 149; HKSAR v Bian Zhenju [2015] 2 HKLRD 1089; R v Bell; R v Davis (Iain Lawrence); DPP (Nauru) v Fowler (1984) 154 CLR 627; Andrew John Hawkins (No 3); Shane Michael Martin (No 4); HKSAR v Ha But-yee FAMC 41/2016, 11 November 2016; HKSAR v Chu Chi-wah; HKSAR v Liang Yaoqiang; HKSAR v Lee Wai-man [2020] 3 HKLRD 310; B (a child) v R and HKSAR v Nayab Amin [2020] 2 HKLRD 1051.

[53] [10].

[54] See, in the context of sentencing, Secretary for Justice v Wong Chi Fung (2018) 21 HKCFAR 35, [62].

[55] Original footnote included.

[56] CA judgment, [7] per Macrae VP.

[57] Ibid, [257](10), per Zervos JA.

[58] Ibid, [124].

[59] Ibid, [252].

[60] Extracted by Zervos JA in [208] of his judgment.

[61] CA judgment, [146].

[62] Ibid, [124].

[63] Ibid, [6], [251], [257](10).

[64] Ibid, [251].

[65] Ibid, [129]-[142].

[66] Ibid, [221]-[257].

[67] Au Pui Kuen v Attorney General of Hong Kong, 356G–H, per Lord Diplock.

[68] CA judgment, [133].

[69] A starting point of 27 years discounted by one‑third for an early guilty plea would give a sentence of 18 years.  A one‑third remission for good behaviour would reduce the actual period of imprisonment to 12 years.

[70] See below.

[71] CA judgment, [119].

[72] R v Yu Wing-sze CACC 372/1995, 15 November 1995; HKSAR v Tam Shu-kin CACC 444/2004, 13 May 2005; HKSAR v Yiu Kam‑tin CACC 510/2004, 1 June 2005; HKSAR v Lau Bo‑ki CACC 412/2005, 9 November 2007; HKSAR v Lim Khi‑chong CACC 159/2007, 9 November 2007; HKSAR v Liu Chui-fa HCCC 8/2012, 13 August 2012; HKSAR v Yeung Ki HCCC 242/2013, 14 March 2014; HKSAR v Chen Peng HCCC 115/2016, 20 June 2018; HKSAR v Francisco Reynaldo [2000] 3 HKLRD 688; HKSAR v Wong Kam‑shing Jackie [2010] 4 HKC 580; HKSAR v Yau Kit‑keung [2010] 6 HKC 473.

[73] HKSAR v Lau Bo‑ki, [11], a case of total denial of responsibility for the killing.

                         """)


def test_api_connection():
    with st.spinner('Loading...'):
        response = requests.get("http://backend:5001/health").json()
        if response.get('status') != 'ok':
            return 'error'
    return response


def load_response_from_api(case, reference):
    with st.spinner('Loading...'):
        response = requests.post(
            "http://backend:5001/analyseCase", json={'case': case, 'reference': reference}).json()

        if response.get('status') != 'ok':
            logger.error(response)
            return 'error'
    return response.get('result')


if st.button('Test conenction'):
    response = test_api_connection()
    st.write(response)

if st.button('Analyse'):
    response = load_response_from_api(case, reference)
    if response == 'error':
        st.write(response)
    else:
        summary = response['summary_string']
        reference = response['reference_dict']
        foot_notes = response['footnote_data']

        for sl in summary.split('\n'):
            if sl in reference:
                with st.expander(sl):
                    st.write(f'''{reference[sl]}''')
            else:
                st.write(sl)

        st.write("**References**")
        for fn in foot_notes:
            with st.expander(fn['footnotes_texts']):
                st.write(f'''{fn["sentence"]}''')
