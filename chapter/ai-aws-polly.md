# AWS Polly sp20-516-236, Achath, Seema

## Introduction to Amazon Polly

Text-to-speech (TTS) can help create more useful and accessible content. Even few years back, in order to create voice blogs, there was a need for recording equipment and people had to spend hours recording and editing each narration. But with the development of artificial intelligence, text-to-speech benefits can be obtained by spending only a couple of minutes and a few pennies per blog once the text is ready. There are multiple such services offered by various companies including Google, Amazon etc. that are widely available for all to use. One such service is Amazon Polly offered by Amazon Web Services (AWS). AWS is a subsidiary unit of Amazon which provides cloud computing platforms and APIs to individuals, companies, and government organizations, on a metered pay-as-you-go basis. Amazon Polly is a services offered by AWS that turns text into lifelike speech. It enables adding voice to existing applications and also opens up an entirely new avenue for speech-enabled products geared towards mobile apps, cars, variety of devices and appliances. It offers both female and male lifelike voices in many languages. There are multiple options for lifelike voices in multiple languages from which to choose. This opens up opportunities to distribute speech-enabled applications in many geographies.  In addition to Standard TTS voices, Amazon Polly deliver advanced improvements in speech quality through Neural Text-to-Speech (NTTS) voices which is a new machine learning approach. Polly’s NTTS technology also supports a Newscaster reading style (tailored to news narration use cases) and a Conversational speaking style (ideal for two-way communication like telephony applications) that allows better match for the delivery style of the speaker to the application.

## Text-to-Speech (TTS)

This service by AWS is very user friendly and independent. Converting text to an audio stream using this service is just a few clicks away by sending the text that need to be converted to the Amazon Polly API. The API returns the audio stream to your application immediately.  This audio stream can be played directly or it can be stored in a standard audio file format, such as MP3. Amazon Polly supports audio formats such as MP3, Vorbis, and raw PCM audio stream formats. The bandwidth and audio quality can be optimized from various sampling rates that fits well for your application. It also supports Speech Synthesis Markup Language (SSML) tags like prosody. By using SSML, various aspects of speech such as pronunciation, volume, pitch, speech rate, etc. can be controlled. Based on the metadata included in the audio stream, when specific words or sentences in the text are being spoken to the user can be detected. This feature allows the API developer to synchronize graphical highlighting and animations, such as the lip movements of an avatar, with the synthesized speech. It also allows modifying the pronunciation of particular words, such as company names, acronyms, foreign words and neologisms, e.g. "P!nk", "ROTFL", "C’est la vie" (when spoken in a non-French voice) using custom lexicons.

## Languages Supported

Amazon Polly offers both female and male lifelike voices in many languages. It also provides multiple options to choose from in certain languages.  In Amazon Polly, you can select the voice of your choice and distribute your voice enabled applications in many countries. Amazon Polly offers high quality natural and human-like voices using Neural Text-to-Speech (NTTS) voices in addition to the Standard TTS voices. AWS supports 21 languages and 29 distinct language-region pairs. Most regions have one or two voices to select from, where as popular ones like United States English have several options.

Different languages and voice options offered by Amazon Polly   

| Language             | Female                | Male                 |
|----------------------|-----------------------|----------------------|
| Arabic               | Zeina                 |                      |
| Australian English   | Nicole                | Russell              |
| Brazilian Portuguese | Vitória               | Ricardo              |
|                      | Camila \(Standard\)   |                      |
|                      | Camila \(Neural\)     |                      |
| Canadian French      | Chantal               |                      |
| Danish               | Naja                  | Mads                 |
| Dutch                | Lotte                 | Ruben                |
| French               | Léa                   | Mathieu              |
|                      | Céline                |                      |
| German               | Vicki                 | Hans                 |
|                      | Marlene               |                      |
| Hindi                | Aditi                 |                      |
| Icelandic            | Dóra                  | Karl                 |
| Indian English       | Raveena               |                      |
|                      | Aditi                 |                      |
| Italian              | Carla                 | Giorgio              |
|                      | Bianca                |                      |
| Japanese             | Mizuki                | Takumi               |
| Korean               | Seoyeon               |                      |
| Mandarin Chinese     | Zhiyu                 |                      |
| Norwegian            | Liv                   |                      |
| Polish               | Ewa                   | Jacek                |
|                      | Maja                  | Jan                  |
| Portuguese \- Iberic | Inês                  | Cristiano            |
| Romanian             | Carmen                |                      |
| Russian              | Tatyana               | Maxim                |
| Spanish \- Castilian | Conchita              | Enrique              |
|                      | Lucia                 |                      |
| Spanish \- Mexican   | Mia                   |                      |
| Swedish              | Astrid                |                      |
| Turkish              | Filiz                 |                      |
| UK English           | Amy \(Standard\)      | Brian \(Standard\)   |
|                      | Amy \(Neural\)        | Brian \(Neural\)     |
|                      | Emma \(Standard\)     |                      |
|                      | Emma \(Neural\)       |                      |
| US English           | Joanna \(Standard\)   | Matthew \(Standard\) |
|                      | Joanna \(Neural\)     | Matthew \(Neural\)   |
|                      | Salli \(Standard\)    | Justin \(Standard\)  |
|                      | Salli \(Neural\)      | Justin \(Neural\)    |
|                      | Kendra \(Standard\)   | Joey \(Standard\)    |
|                      | Kendra \(Neural\)     | Joey \(Neural\)      |
|                      | Kimberly \(Standard\) |                      |
|                      | Kimberly \(Neural\)   |                      |
|                      | Ivy \(Standard\)      |                      |
|                      | Ivy \(Neural\)        |                      |
| US Spanish           | Penélope              | Miguel               |
|                      | Lupe \(Standard\)     |                      |
|                      | Lupe \(Neural\)       |                      |
| Welsh                | Gwyneth               |                      |
| Welsh English        |                       | Geraint              |

## Speech Marks

Speech marks or inverted commas are used to complement the synthesized speech that is generated from the input text.  These are designed to show what the words actually spoken by a person or character are.  The words spoken directly are marked by speech marks.  Polly uses the synthesized speech audio stream together with metadata, to provide enhanced visual experience such as speech-synchronized animation or karaoke-style highlighting for customers to use in their applications. For this speech marks, as many as four types of metada can be requested in Amazon Polly.

*	sentence – Indicates a sentence element in the input text.
*	word – Indicates a word element in the text.
*	viseme – Describes the face and mouth movements corresponding to each phoneme being spoken.
*	SSML – Describes an element from the SSML input text.

In Polly these Speech Marks are delivered in form of a JSON stream (a set of standalone JSON objects delimited with new lines) containing anywhere from one to all four of these elements given above. Some of the programming languages supported by Polly are included in the AWS SDK (Java, Node.js, .NET, PHP, Python, Ruby, Go, and C++) and AWS Mobile SDK (iOS/Android). Amazon Polly also supports an HTTP API to implement the user’s own access layer.

AWS Transcribe which is a speech-to-text option in AWS, transcribes long audio sources like podcasts and interviews which will take a long time using normal means. This AWS service gives an exact opposite to what Amazon Polly offers. When you are listening to an interesting podcast or interview, you hardly listen to them several times. If you want to revisit a certain portions of the podcast/ interview, a transcript will be easy to reread and reference it. Thus AWS Transcribe provides that option to the customers. 

## Benefits

Using text-to-speech, the developers can give more life to their applications and the users can have a better experience when working on the applications as well. For example, such systems can be used in telephony solutions to Voice Interactive Voice Response systems. Amazon Polly like services are a boon to people with reading disabilities particularly in the E-learning and education sector. Polly can be used to help the blind and visually impaired people consume digital content (eBooks, news etc.). Using such systems, a visually impaired or people with leaning disorder (dyslexic) can benefit more from a narrated version of an article, while a deaf person could read a transcript of the podcast and become a member of the show. It can also be used in public transportation and industrial control announcement systems for notifications and emergency announcements. In addition to these, devices such as smartphones, set-top boxes, smart watches, tablets, and Internet-of-Things (IoT) devices, which can leverage such services for providing audio output. For developers, Amazon Polly can be combined with other AWS products such as Amazon Lex or Connect, to create full-blown Voice User Interfaces for their applications or to create self-service cloud-based contact center services. 

## Advantages of Amazon Polly

One of the primary reason for using Amazon Polly is that you can power your application with high-quality voice output. Its cost-effective service has very low response times, lack of restrictions on storage and reuse of audio stream and is virtually available for any type of applications. This AWS service is secure and provides all of these benefits at high scale and low latency. You can cache the audio stream and replay it on your APIs at no additional cost. As far as the cost is concerned, upon sign up, Polly lets you convert 5M characters for free per month during the first year. Amazon Polly’s low cost, pay-as-you-go pricing, and lack of restrictions on storage and reuse of audio stream make it a cost-effective way to enable voice applications everywhere.

## Cloud services

Amazon Polly offers all these advantages in cloud-based platform which offers a significant improvement over an on-device one. In on-device, for example smart phones, tablets etc. applications require significant computing resources, notably CPU power, RAM, and disk space. This can result in higher development cost and higher power consumption. In contrast, if these text-to-speech transformations are carried out in the cloud, local resource requirements are dramatically reduced. This allows voices at the highest possible quality in multiple languages possible without any additional updates.

## Getting started in Polly

Getting started with AWS is simple. Once an account in AWS is created, simply navigate to the Amazon Polly console (which is a part of the AWS Console) after login. 

<https://us-east-1.console.aws.amazon.com/polly/home/SynthesizeSpeech>

This console can be used to transform the text to generate an audio file which can then be used or stored.

! [Fig. Image of the opening page of the Amazon polly console] (../images/Pollygetstarted.png)
 
A detailed description of the regions in which the service is available is provide in the AWS Global Infrastructure Region Table. 

<https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/>

In order to make sure, the availability of AWS resources and to avoid billing risk for new customers, there are default service limits including limitations on throttling, operations, and Speech Synthesis Markup Language (SSML) use. To circumvent these limitation, Polly can be combined with other AWS services, such as AWS Batch for efficient batch processing.

<https://docs.aws.amazon.com/polly/latest/dg/limits.html>

Amazon Poly uses a pay-as-you-go model. The monthly bill is for the number of characters of text that was processed. Standard voices are priced at $4.00 per 1 million characters for speech or Speech Marks requests (when outside the free tier). For Neural voices, the free tier includes 1 million characters per month for speech or Speech Marks requests, for the first 12 months, starting from your first request for speech. Amazon Polly’s Neural voices are priced at $16.00 per 1 million characters for speech or Speech Marks requested (when outside the free tier). A detailed Polly pricing is given in

<https://aws.amazon.com/polly/pricing/>

Amazon Polly also offers a brand voice choice as an option. This allows people or companies to develop their own brand of voice which can then be used for their application. To develop own brand, it is important to understand the goals to accurately scope a Brand Voice engagement. So in case you are interested in building a brand voice using Amazon Polly, need to contact AWS Account Manager or AWS directly.

## References

1. <https://www.smashingmagazine.com/2019/08/text-to-speech-aws/>

2. <https://aws.amazon.com/polly/faqs/>

3. <https://aws.amazon.com/blogs/aws/amazon-polly-introduces-neural-text-to-speech-and-newscaster-style/>
