# *** This file is generated by pseudoadiabat_codegen/pseudoadiabat_codegen.py ***
# *** Please ensure any updates are made in pseudoadiabat_codegen.py           ***
import numpy as np
from numba import vectorize


@vectorize(nopython=True, cache=True)
def wbpt(p, T):
    """
    Computes the wet-bulb potential temperature (WBPT) thw of the
    pseudoadiabat that passes through pressure p and temperature T.

    Uses polynomial approximations from Moisseeva and Stull (2017)
    with revised coefficients.

    Moisseeva, N. and Stull, R., 2017. A noniterative approach to
        modelling moist thermodynamics. Atmospheric Chemistry and
        Physics, 17, 15037-15043.

    Args:
        p: pressure (Pa)
        T: temperature (K)

    Returns:
        thw: wet-bulb potential temperature (K)

    """

    # Convert p to hPa and T to degC
    p_ = p / 100.
    T_ = T - 273.15

    # Check that values fall in the permitted range
    if (T_ < -100.) or (T_ > 50.) or (p_ > 1100.) or (p_ < 50.):
        # print('T or p outside limits of polynomial fit', T_, p_)
        return np.nan

    # Compute theta-w using Eq. 4-6 from Moisseeva & Stull 2017
    Tref = 5.545194269969744028e+01 + p_*(-6.160922643206258043e-01 + p_*(7.587811691476412448e-03 + p_*(-8.979212604246789573e-05 + p_*(7.343181162799252997e-07 + p_*(-4.203811338238339756e-09 + p_*(1.680461676878753079e-11 + p_*(-4.663028376804742115e-14 + p_*(8.792987053284386843e-17 + p_*(-1.047685061993484244e-19 + p_*(5.803471746171544039e-23 + p_*(2.719984341254661375e-26 + p_*(-6.275663461476053709e-29 + p_*(1.325022483616707296e-32 + p_*(4.338742237555935124e-35 + p_*(-3.090431264151296911e-38 + p_*(-2.003198659255209158e-41 + p_*(4.151977079563261066e-44 + p_*(-2.671125528966892761e-47 + p_*(8.274902032133455127e-51 + p_*(-1.046220932987381136e-54))))))))))))))))))))  # noqa: E501
    thw = 4.232940944232577607e+01 + T_*(5.718057512715307711e-01 + T_*(6.676677597885334776e-03 + T_*(4.022328480366987597e-05 + T_*(-9.508933019160445564e-07 + T_*(-7.872837881810170976e-09 + T_*(1.764981358907121684e-10 + T_*(2.337314128547671647e-12 + T_*(-3.546237055245935149e-14 + T_*(-6.653359895702736545e-16 + T_*(5.416100578454232859e-18 + T_*(1.736801137333358149e-19 + T_*(-1.614941755022829075e-22 + T_*(-3.466397463900693713e-23 + T_*(-1.954775222373624531e-25 + T_*(3.917994330304135765e-27 + T_*(5.062948051510256424e-29 + T_*(-4.425505843709759732e-32 + T_*(-4.099457794462657487e-33 + T_*(-2.659946576039995724e-35 + T_*(-5.616686551472560432e-38)))))))))))))))))))) + Tref*(3.623382401650120932e-01 + T_*(1.023543556426264028e-03 + T_*(7.651560288975466182e-05 + T_*(-3.333050342938257735e-07 + T_*(-1.155276051647147619e-08 + T_*(5.929972799181639469e-11 + T_*(3.206717543550327453e-12 + T_*(-2.806173962086747008e-15 + T_*(-5.124959937929081926e-16 + T_*(-1.855121616602876157e-17 + T_*(9.821368425617630502e-20 + T_*(1.227932266156539288e-20 + T_*(-7.683681814109954133e-24 + T_*(-4.104781036660294525e-24 + T_*(-1.459303936349590696e-26 + T_*(7.195188421056683942e-28 + T_*(6.308529814583321843e-30 + T_*(-3.728722888842601765e-32 + T_*(-7.651013597331745427e-34 + T_*(-3.900687460769850595e-36 + T_*(-6.838418124460199041e-39)))))))))))))))))))) + Tref*(2.901311619805157452e-03 + T_*(6.485698819407039969e-05 + T_*(7.728091544277208254e-07 + T_*(-9.073366523455469539e-09 + T_*(-2.141374965578981410e-10 + T_*(3.977216429327843141e-12 + T_*(4.122840262503433229e-14 + T_*(-5.256646599001689577e-16 + T_*(-1.145434112370376915e-17 + T_*(-1.781311250561409403e-19 + T_*(7.157635199010274020e-21 + T_*(8.010843921970355959e-23 + T_*(-2.967462937546381677e-24 + T_*(-1.231180428827811944e-26 + T_*(7.411974321317298560e-28 + T_*(1.871989870585702621e-30 + T_*(-1.139473166366657039e-31 + T_*(-5.550450159434532228e-34 + T_*(7.751320464793886659e-36 + T_*(7.636712088445193183e-38 + T_*(1.904910678489293722e-40)))))))))))))))))))) + Tref*(6.704619097436729624e-05 + T_*(1.163029842424645954e-06 + T_*(1.492287334118758421e-08 + T_*(-9.803556343362327257e-11 + T_*(-5.321938015151650545e-12 + T_*(-8.750285129654440476e-14 + T_*(7.883547117854788030e-15 + T_*(-1.969218043870929035e-17 + T_*(-5.127731809674121555e-18 + T_*(7.842500025808431793e-20 + T_*(1.656834067909569676e-21 + T_*(-4.771060315991388879e-23 + T_*(-3.789330073585334101e-25 + T_*(1.503827044450349823e-26 + T_*(1.063631966232871725e-28 + T_*(-2.515473868945231314e-30 + T_*(-2.685544596332960150e-32 + T_*(1.185962932727380623e-34 + T_*(2.890950955818082802e-36 + T_*(1.500601905017281505e-38 + T_*(2.612549730540674067e-41)))))))))))))))))))) + Tref*(5.622752095209163301e-07 + T_*(2.622299773664040882e-08 + T_*(1.305336393284960921e-10 + T_*(-1.276960779075757062e-12 + T_*(-1.683548375977049797e-13 + T_*(-6.271150950803480645e-16 + T_*(2.315028031157249709e-16 + T_*(-2.146347028376092958e-18 + T_*(-1.245693873642227093e-19 + T_*(2.045375912756655024e-21 + T_*(3.384747838730439315e-23 + T_*(-7.402265189368336296e-25 + T_*(-5.511288828625452761e-27 + T_*(1.398311724960150295e-28 + T_*(5.941982483198068820e-31 + T_*(-1.481882184010474742e-32 + T_*(-3.464262458502697741e-35 + T_*(9.867780531525398202e-37 + T_*(6.017124351539231275e-40 + T_*(-5.595813431706730079e-41 + T_*(-2.065635042206331018e-43)))))))))))))))))))) + Tref*(6.310399231532088346e-09 + T_*(3.901231962638336016e-10 + T_*(4.180122829870311996e-12 + T_*(-3.192353977095813438e-13 + T_*(9.004741911651702877e-16 + T_*(3.149258318289430785e-16 + T_*(-7.025210952408942387e-18 + T_*(-6.361263629427768113e-20 + T_*(5.124872290307491148e-21 + T_*(-7.054075409523944098e-23 + T_*(-1.553787992819717914e-24 + T_*(5.585474476756643726e-26 + T_*(3.240541368795211673e-28 + T_*(-1.953300445074685362e-29 + T_*(-1.131145285513222428e-31 + T_*(3.507374001441693019e-33 + T_*(3.473614062208678184e-35 + T_*(-1.806024510910001329e-37 + T_*(-4.054752894421383860e-39 + T_*(-2.101330765235148035e-41 + T_*(-3.695013142657365282e-44)))))))))))))))))))) + Tref*(1.271719593514502614e-10 + T_*(6.212652945668079643e-12 + T_*(4.718325172207772923e-14 + T_*(-9.049900408478350932e-15 + T_*(1.581335742011448829e-16 + T_*(7.664434600667353565e-18 + T_*(-3.032068138918179548e-19 + T_*(-2.954470910946507580e-23 + T_*(1.764470276812099321e-22 + T_*(-2.362502682406429885e-24 + T_*(-4.810519050498481162e-26 + T_*(1.293799446056060717e-27 + T_*(8.263862859728115334e-30 + T_*(-3.703475842686161888e-31 + T_*(-1.875235811381363166e-33 + T_*(5.999930281812112887e-35 + T_*(4.929459653637661333e-37 + T_*(-3.378361077097880353e-39 + T_*(-5.686371346389453665e-41 + T_*(-2.469609650556775141e-43 + T_*(-3.483253301441309733e-46)))))))))))))))))))) + Tref*(3.006868042816497974e-12 + T_*(6.996687305913599728e-14 + T_*(-1.902923934541224379e-15 + T_*(2.538423830307459436e-18 + T_*(2.175603590409096192e-18 + T_*(-4.327281625931597660e-20 + T_*(-2.645614098017516364e-22 + T_*(1.558894913470146477e-23 + T_*(-3.942387509153589096e-25 + T_*(1.606988956610959619e-26 + T_*(1.540754199772559106e-28 + T_*(-1.543468479057767344e-29 + T_*(-4.922832778131969665e-32 + T_*(5.943402637170408262e-33 + T_*(3.300968515126008702e-35 + T_*(-1.109485447615582067e-36 + T_*(-1.161425587366964164e-38 + T_*(5.384616121931944142e-41 + T_*(1.368792887313021082e-42 + T_*(7.550551701298664713e-45 + T_*(1.415937577614429599e-47)))))))))))))))))))) + Tref*(4.182255148516593461e-14 + T_*(3.264676233541051175e-16 + T_*(-5.820220450542899159e-17 + T_*(3.026293244201152484e-18 + T_*(-1.682107528877679333e-20 + T_*(-3.123096672164356461e-21 + T_*(1.015072165615557285e-22 + T_*(-1.617560469774974781e-27 + T_*(-6.536703646025585238e-26 + T_*(1.186271179408631216e-27 + T_*(1.783041190999098461e-29 + T_*(-7.191842428389848484e-31 + T_*(-3.361306213352488339e-33 + T_*(2.262717601618277057e-34 + T_*(1.148352949368445723e-36 + T_*(-3.863263832687730034e-38 + T_*(-3.541738215440329823e-40 + T_*(2.021964051892091788e-42 + T_*(4.128740907197908282e-44 + T_*(2.049947393504634744e-46 + T_*(3.458727452025841363e-49)))))))))))))))))))) + Tref*(3.112534666153723136e-16 + T_*(-1.873677837019567290e-18 + T_*(-5.532179823077458254e-19 + T_*(3.972525584479210441e-20 + T_*(-5.188987892734337527e-22 + T_*(-3.391862596574743670e-23 + T_*(1.360453159001269833e-24 + T_*(-3.242112215867949590e-27 + T_*(-7.896373372992186301e-28 + T_*(1.390393221833685870e-29 + T_*(2.076015827047371213e-31 + T_*(-7.560992513098718830e-33 + T_*(-3.706163991610245534e-35 + T_*(2.232620184844021166e-36 + T_*(1.100559065706659980e-38 + T_*(-3.682533656835250976e-40 + T_*(-3.223844945267788809e-42 + T_*(1.959334144661060940e-44 + T_*(3.724119862112135153e-46 + T_*(1.769242397715477826e-48 + T_*(2.834630967748369536e-51)))))))))))))))))))) + Tref*(9.411328600369717429e-19 + T_*(-1.894119309117077157e-20 + T_*(-1.690159920349779348e-21 + T_*(1.555805697490074380e-22 + T_*(-2.709557222214898465e-24 + T_*(-1.153517854329395671e-25 + T_*(5.376287143187457606e-27 + T_*(-2.108474084097347475e-29 + T_*(-2.936789306313718369e-30 + T_*(5.194452993306611497e-32 + T_*(7.564143480889889416e-34 + T_*(-2.625235896598812213e-35 + T_*(-1.323767432812173567e-37 + T_*(7.405986542712064772e-39 + T_*(3.613468467711806690e-41 + T_*(-1.187961459658149567e-42 + T_*(-1.011384549214553935e-44 + T_*(6.348852099821227991e-47 + T_*(1.153959216106457934e-48 + T_*(5.305336228574541091e-51 + T_*(8.145685183982982076e-54))))))))))))))))))))))))))))))  # noqa: E501

    # Return theta-w converted to K
    return thw + 273.15


@vectorize(nopython=True, cache=True)
def temp(p, thw):
    """
    Computes the temperature T at pressure p on a pseudoadiabat with
    wet-bulb potential temperature thw.

    Uses polynomial approximations from Moisseeva and Stull (2017) with
    revised coefficients.

    Moisseeva, N. and Stull, R., 2017. A noniterative approach to
        modelling moist thermodynamics. Atmospheric Chemistry and
        Physics, 17, 15037-15043.

    Args:
        p: pressure (Pa)
        thw: wet-bulb potential temperature (K)

    Returns:
        T: temperature (K)

    """

    # Convert p to hPa and theta-w to degC
    p_ = p / 100.
    thw_ = thw - 273.15

    # Check that values fall in the permitted range
    if (thw_ < -70.) or (thw_ > 50.) or (p_ > 1100.) or (p_ < 50.):
        # print('thw or p outside limits of polynomial fit', thw_, p_)
        return np.nan

    # Compute T using Eq. 1-3 from Moisseeva & Stull 2017
    thref = -1.937920800653422475e+02 + p_*(1.994328166933734936e+00 + p_*(-2.237013575312922151e-02 + p_*(2.161737851675146153e-04 + p_*(-1.538607021098927656e-06 + p_*(7.955260853377150502e-09 + p_*(-2.983279520973976083e-11 + p_*(8.039566675064638876e-14 + p_*(-1.515292673478941849e-16 + p_*(1.854100168418495209e-19 + p_*(-1.115026192870100507e-22 + p_*(-3.969971732515197016e-26 + p_*(1.161169755869383278e-28 + p_*(-3.444083207986219187e-32 + p_*(-7.866653966250901723e-35 + p_*(6.625041435759308529e-38 + p_*(3.366795656456184692e-41 + p_*(-8.457678956195843103e-44 + p_*(5.836181847569190006e-47 + p_*(-1.910491737787847276e-50 + p_*(2.538391257078461717e-54))))))))))))))))))))  # noqa: E501
    T = -2.894809154394712181e+01 + thw_*(1.336650338083321898e+00 + thw_*(9.920943036173456367e-03 + thw_*(-5.531214167407858472e-05 + thw_*(-8.119357346521603519e-06 + thw_*(-1.620387392038411444e-07 + thw_*(4.037532909615920346e-09 + thw_*(2.733163059497750080e-10 + thw_*(9.427391543821474143e-13 + thw_*(-2.327854753793110044e-13 + thw_*(-3.504745859399798296e-15 + thw_*(1.108525038070919562e-16 + thw_*(2.815122082998062845e-18 + thw_*(-2.331111962009056858e-20 + thw_*(-1.138455622006271100e-21 + thw_*(-2.121842082147546585e-24 + thw_*(2.276656333522116348e-25 + thw_*(1.935220598348594753e-27 + thw_*(-1.435126816259871481e-29 + thw_*(-2.595738870945626914e-31 + thw_*(-9.691377297361992261e-34)))))))))))))))))))) + thref*(1.428881737537489149e+00 + thw_*(-7.928369124218480335e-03 + thw_*(-6.836727328681309508e-04 + thw_*(-1.575778513934627693e-05 + thw_*(2.363089166681158867e-07 + thw_*(3.377370448942234055e-08 + thw_*(6.763932007194685287e-10 + thw_*(-3.404787955461038834e-11 + thw_*(-1.392897110579503108e-12 + thw_*(1.754731183379382578e-14 + thw_*(1.325210356297305846e-15 + thw_*(-9.979176873736201255e-19 + thw_*(-7.316075852388014696e-19 + thw_*(-4.367591110344463074e-21 + thw_*(2.329382669197465213e-22 + thw_*(2.612519003597594999e-24 + thw_*(-3.663141187578808357e-26 + thw_*(-6.500140433674884368e-28 + thw_*(9.818511911722120689e-31 + thw_*(6.214415118411740173e-32 + thw_*(2.876486598268410161e-34)))))))))))))))))))) + thref*(4.972737015894919572e-03 + thw_*(-5.180031163839903972e-04 + thw_*(-8.443354080975294695e-06 + thw_*(6.970604985870997408e-07 + thw_*(4.745538679375798390e-08 + thw_*(3.605934838576005089e-10 + thw_*(-8.294489100400780575e-11 + thw_*(-2.420658446084975386e-12 + thw_*(6.731764854037241284e-14 + thw_*(3.351958552392139447e-15 + thw_*(-1.800972624739673327e-17 + thw_*(-2.324301238607420061e-18 + thw_*(-1.072851574806577385e-20 + thw_*(8.560224907361107825e-22 + thw_*(9.874192461006248167e-24 + thw_*(-1.414588503720268695e-25 + thw_*(-2.876521559727777627e-27 + thw_*(6.403220467343629572e-32 + thw_*(2.884475470792268876e-31 + thw_*(1.985478640920712375e-33 + thw_*(3.502058845458745414e-36)))))))))))))))))))) + thref*(-1.699534078374525885e-04 + thw_*(-3.900689915192402402e-06 + thw_*(7.214960588486119121e-07 + thw_*(3.788345751455296015e-08 + thw_*(-6.273481073442938028e-10 + thw_*(-1.214840085243346332e-10 + thw_*(-1.807232389121394695e-12 + thw_*(1.857449223972803575e-13 + thw_*(5.417783359399633895e-15 + thw_*(-1.472967199669265098e-16 + thw_*(-6.415493945575949307e-18 + thw_*(5.039132448915254268e-20 + thw_*(4.125098114685523165e-21 + thw_*(6.886806005805598986e-24 + thw_*(-1.478684652781221744e-24 + thw_*(-1.179343694500363276e-26 + thw_*(2.618396835490149079e-28 + thw_*(3.680001891075254443e-30 + thw_*(-1.108975483763781084e-32 + thw_*(-3.931760167079157084e-34 + thw_*(-1.718553853952838073e-36)))))))))))))))))))) + thref*(-3.325925800984791198e-06 + thw_*(2.450733346832845189e-07 + thw_*(2.215366969237199514e-08 + thw_*(-2.737615636676214507e-10 + thw_*(-9.250840980982384768e-11 + thw_*(-1.809819952947534347e-12 + thw_*(1.795487723452759831e-13 + thw_*(6.173650129477465262e-15 + thw_*(-1.701344681053855650e-16 + thw_*(-8.494797520341489610e-18 + thw_*(6.357161726488955308e-20 + thw_*(6.183553852752261233e-21 + thw_*(1.538679053848080909e-23 + thw_*(-2.438981420752364444e-24 + thw_*(-2.230971768664982437e-26 + thw_*(4.571162612759753901e-28 + thw_*(7.297138929988679687e-30 + thw_*(-1.572635491856643009e-32 + thw_*(-8.087623670303043750e-34 + thw_*(-4.271209690350353269e-36 + thw_*(-3.314300903114658836e-39)))))))))))))))))))) + thref*(3.414616856301753333e-08 + thw_*(6.268580800459015886e-09 + thw_*(-1.580414880896166803e-10 + thw_*(-3.678514556327383886e-11 + thw_*(-6.675021176897811867e-13 + thw_*(1.012337614818958783e-13 + thw_*(3.961263281808238210e-15 + thw_*(-1.381645980256255610e-16 + thw_*(-7.875887580502500946e-18 + thw_*(8.513951910182300971e-20 + thw_*(8.177221172048067876e-21 + thw_*(-8.703350255131019920e-26 + thw_*(-4.844774877757557582e-24 + thw_*(-3.190640346940055164e-26 + thw_*(1.610996932999312759e-27 + thw_*(1.907049805756753079e-29 + thw_*(-2.575040071002652052e-31 + thw_*(-4.785413537935581317e-33 + thw_*(6.186014275961251495e-36 + thw_*(4.578462095249169054e-37 + thw_*(2.158200510527907784e-39)))))))))))))))))))) + thref*(1.832539084881889899e-09 + thw_*(2.232154349041515070e-11 + thw_*(-1.720691072260209130e-11 + thw_*(-5.962355584738739171e-13 + thw_*(5.843949898672926130e-14 + thw_*(3.115793612394376880e-15 + thw_*(-8.732283600324087146e-17 + thw_*(-6.963438435050066380e-18 + thw_*(4.006495961779091573e-20 + thw_*(8.144337413199188819e-21 + thw_*(4.366031611409002476e-23 + thw_*(-5.234490503853010733e-24 + thw_*(-6.829505960497079623e-26 + thw_*(1.728116462140354231e-27 + thw_*(3.713189734493524910e-29 + thw_*(-1.838398243709750054e-31 + thw_*(-9.166025002345479808e-33 + thw_*(-3.883145420373912959e-35 + thw_*(7.747074099177721883e-37 + thw_*(8.755083691453450219e-39 + thw_*(2.651398973574923431e-41)))))))))))))))))))) + thref*(2.678809287247188447e-11 + thw_*(-9.936336895749793214e-13 + thw_*(-3.331147267147120202e-13 + thw_*(-1.424906631040857522e-15 + thw_*(1.568937881338988438e-15 + thw_*(3.023102970013440824e-17 + thw_*(-3.599415306574552030e-18 + thw_*(-9.462981008148341325e-20 + thw_*(4.378770462977206976e-21 + thw_*(1.396512678567408808e-22 + thw_*(-2.823320460275946884e-24 + thw_*(-1.137831839057805968e-25 + thw_*(8.132223243232400173e-28 + thw_*(5.273046758652151134e-29 + thw_*(2.712801402117304436e-32 + thw_*(-1.324919601404670228e-32 + thw_*(-7.264519583033080077e-35 + thw_*(1.510686767239771840e-36 + thw_*(1.373988911767683650e-38 + thw_*(-3.705871967500240777e-41 + thw_*(-4.980988505967098614e-43)))))))))))))))))))) + thref*(1.989628070690088685e-13 + thw_*(-1.523344650151727583e-14 + thw_*(-3.049694495393029476e-15 + thw_*(4.371888536717950116e-17 + thw_*(1.673864731634620975e-17 + thw_*(7.307645927407795769e-20 + thw_*(-4.423707668937182769e-20 + thw_*(-5.365318477748185415e-22 + thw_*(6.307660745198924017e-23 + thw_*(1.051921483697963415e-24 + thw_*(-5.090997089250726191e-26 + thw_*(-1.045822982223108853e-27 + thw_*(2.299390931720666921e-29 + thw_*(5.856181064117101660e-31 + thw_*(-5.127747701200545643e-33 + thw_*(-1.848983658781484082e-34 + thw_*(2.237846108161224605e-37 + thw_*(3.026680754951921398e-38 + thw_*(1.028290625341324349e-40 + thw_*(-1.947842364396178267e-42 + thw_*(-1.215938016409552301e-44)))))))))))))))))))) + thref*(7.648553716659091758e-16 + thw_*(-8.710548696300586344e-17 + thw_*(-1.384960302031060676e-17 + thw_*(3.953752472780564185e-19 + thw_*(8.363535806701477117e-20 + thw_*(-4.577577613176423449e-22 + thw_*(-2.394890583051712372e-22 + thw_*(-1.013681538018464148e-24 + thw_*(3.696580248182901828e-25 + thw_*(3.612583836691359672e-27 + thw_*(-3.265586466259759211e-28 + thw_*(-4.523940336584103313e-30 + thw_*(1.663325208493514205e-31 + thw_*(2.961550524803013470e-33 + thw_*(-4.566581435837660283e-35 + thw_*(-1.072435365589353776e-36 + thw_*(4.925056055046214252e-39 + thw_*(2.027553955194815686e-40 + thw_*(3.341279110766656890e-43 + thw_*(-1.556569362026769510e-44 + thw_*(-8.619061688502930173e-47)))))))))))))))))))) + thref*(1.209668896797693583e-18 + thw_*(-1.820592893624389411e-19 + thw_*(-2.511342379897640287e-20 + thw_*(1.010039918014097075e-21 + thw_*(1.620519955904728492e-22 + thw_*(-2.087854511890771101e-24 + thw_*(-4.895653838936800837e-25 + thw_*(5.810948626229826322e-28 + thw_*(7.948112235807493652e-28 + thw_*(4.372796890258928390e-30 + thw_*(-7.403655384903163203e-31 + thw_*(-7.554231171010766963e-33 + thw_*(4.011562970961407727e-34 + thw_*(5.725988369219874812e-36 + thw_*(-1.199729053573629101e-37 + thw_*(-2.293705058593750521e-39 + thw_*(1.567359307437282233e-41 + thw_*(4.724987348794075787e-43 + thw_*(3.401927490570441596e-46 + thw_*(-3.943223448362956556e-47 + thw_*(-2.070180466386040082e-49))))))))))))))))))))))))))))))  # noqa: E501

    # Return T converted to K
    return T + 273.15