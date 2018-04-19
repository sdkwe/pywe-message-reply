# -*- coding: utf-8 -*-

import collections

from pywe_xml import dict_to_xml
from TimeConvert import TimeConvert as tc


class Reply(object):
    def text(self, touser=None, fromuser=None, content=None):
        """
        <xml>
            <ToUserName>< ![CDATA[toUser] ]></ToUserName>
            <FromUserName>< ![CDATA[fromUser] ]></FromUserName>
            <CreateTime>12345678</CreateTime>
            <MsgType>< ![CDATA[text] ]></MsgType>
            <Content>< ![CDATA[你好] ]></Content>
        </xml>
        """
        return dict_to_xml(collections.OrderedDict([
            ('ToUserName', touser),
            ('FromUserName', fromuser),
            ('CreateTime', tc.utc_timestamp()),
            ('MsgType', 'text'),
            ('Content', content)
        ]))

    def image(self):
        """
        <xml>
            <ToUserName>< ![CDATA[toUser] ]></ToUserName>
            <FromUserName>< ![CDATA[fromUser] ]></FromUserName>
            <CreateTime>12345678</CreateTime>
            <MsgType>< ![CDATA[image] ]></MsgType>
            <Image>
                <MediaId>< ![CDATA[media_id] ]></MediaId>
            </Image>
        </xml>
        """

    def voice(self):
        """
        <xml>
            <ToUserName>< ![CDATA[toUser] ]></ToUserName>
            <FromUserName>< ![CDATA[fromUser] ]></FromUserName>
            <CreateTime>12345678</CreateTime>
            <MsgType>< ![CDATA[voice] ]></MsgType>
            <Voice>
                <MediaId>< ![CDATA[media_id] ]></MediaId>
            </Voice>
        </xml>
        """

    def video(self):
        """
        <xml>
            <ToUserName>< ![CDATA[toUser] ]></ToUserName>
            <FromUserName>< ![CDATA[fromUser] ]></FromUserName>
            <CreateTime>12345678</CreateTime>
            <MsgType>< ![CDATA[video] ]></MsgType>
            <Video>
                <MediaId>< ![CDATA[media_id] ]></MediaId>
                <Title>< ![CDATA[title] ]></Title>
                <Description>< ![CDATA[description] ]></Description>
            </Video>
        </xml>
        """

    def music(self):
        """
        <xml>
            <ToUserName>< ![CDATA[toUser] ]></ToUserName>
            <FromUserName>< ![CDATA[fromUser] ]></FromUserName>
            <CreateTime>12345678</CreateTime>
            <MsgType>< ![CDATA[music] ]></MsgType>
            <Music>
                <Title>< ![CDATA[TITLE] ]></Title>
                <Description>< ![CDATA[DESCRIPTION] ]></Description>
                <MusicUrl>< ![CDATA[MUSIC_Url] ]></MusicUrl>
                <HQMusicUrl>< ![CDATA[HQ_MUSIC_Url] ]></HQMusicUrl>
                <ThumbMediaId>< ![CDATA[media_id] ]></ThumbMediaId>
            </Music>
        </xml>
        """

    def news(self):
        """
        <xml>
            <ToUserName>< ![CDATA[toUser] ]></ToUserName>
            <FromUserName>< ![CDATA[fromUser] ]></FromUserName>
            <CreateTime>12345678</CreateTime>
            <MsgType>< ![CDATA[news] ]></MsgType>
            <ArticleCount>2</ArticleCount>
            <Articles>
                <item>
                    <Title>< ![CDATA[title1] ]></Title>
                    <Description>< ![CDATA[description1] ]></Description>
                    <PicUrl>< ![CDATA[picurl] ]></PicUrl>
                    <Url>< ![CDATA[url] ]></Url>
                </item>
                <item>
                    <Title>< ![CDATA[title] ]></Title>
                    <Description>< ![CDATA[description] ]></Description>
                    <PicUrl>< ![CDATA[picurl] ]></PicUrl>
                    <Url>< ![CDATA[url] ]></Url>
                </item>
            </Articles>
        </xml>
        """


reply = Reply()
reply_text = reply.text
