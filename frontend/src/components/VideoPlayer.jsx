import React from "react";
import { Player, Ui, Video } from '@vime/react';
import '@vime/core/themes/default.css';
import './video.css'
export default function VideoPlayer(){
    return(
        <div className="videoplayer">
            <Player id="player" controls>
                <Video crossOrigin="" poster="https://media.vimejs.com/poster.png">
                    <source
                        data-src="http://localhost:8000/video/particulas.mp4"
                        type="video/mp4"
                    />
                </Video>
            </Player>
        </div>
    
    );
    
}