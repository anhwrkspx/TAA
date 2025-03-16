import { ScrollArea} from '@/components/ui/scroll-area'
import React,{ReactNode} from 'react'

interface ShowChatProps{
    children:ReactNode
}

const ShowChat =({children}: ShowChatProps) =>{
    return (
        <>
            <ScrollArea className='container mx-auto h-[70vh] bg-cyan-50 rounded-md'>
                {children}
            </ScrollArea>
        </>
    )
}

export default ShowChat;