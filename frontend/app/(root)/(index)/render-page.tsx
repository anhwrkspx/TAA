"use client"
import React, { useState } from 'react'
import InputChat from './components/input-chat'
import MessChat from './components/mess-chat'
import ShowChat from './components/show-chat'
const RenderPage = () => {
    const [mess, setMess] = useState<string[]>([])
    const [result, setResult] = useState<string[]>([])
    console.log(mess)
    console.log(result)
    return (
        <main className="py-10">
            <ShowChat>
                {mess && (
                    mess.map((item, index) => (
                        <React.Fragment key={`message-group-${index}`}>
                            <MessChat
                                key={`user-${index}`}
                                result={item}
                                role='user'
                            />
                            {result[index] && (
                                <MessChat
                                    key={`ai-${index}`}
                                    result={result[index]}
                                    role='ai'
                                />
                            )}
                        </React.Fragment>

                    )))}
            </ShowChat>
            <InputChat
                onChangeMess={setMess}
                onChangeResult={setResult} />

        </main >
    )
}


export default RenderPage